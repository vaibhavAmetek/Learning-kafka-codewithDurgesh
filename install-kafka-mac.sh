#!/bin/bash

#################################################
# Apache Kafka Installation Script for macOS
# Author: Learning Kafka with Durgesh
# Description: Automated Kafka setup script
#################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored messages
print_message() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

# Check if running on macOS
check_os() {
    print_header "Step 1: Checking Operating System"
    if [[ "$OSTYPE" != "darwin"* ]]; then
        print_error "This script is designed for macOS only!"
        exit 1
    fi
    print_message "Operating System: macOS ✓"
}

# Check Java installation
check_java() {
    print_header "Step 2: Checking Java Installation"
    
    if ! command -v java &> /dev/null; then
        print_warning "Java is not installed!"
        print_message "Installing OpenJDK 17 via Homebrew..."
        brew install openjdk@17
        
        # Set JAVA_HOME
        echo 'export JAVA_HOME="/opt/homebrew/opt/openjdk@17"' >> ~/.zshrc
        echo 'export PATH="$JAVA_HOME/bin:$PATH"' >> ~/.zshrc
        source ~/.zshrc
        
        print_message "Java installed successfully ✓"
    else
        JAVA_VERSION=$(java -version 2>&1 | head -n 1 | cut -d'"' -f2 | cut -d'.' -f1)
        if [ "$JAVA_VERSION" -lt 17 ]; then
            print_warning "Java version is less than 17. Upgrading..."
            brew install openjdk@17
        else
            print_message "Java version: $(java -version 2>&1 | head -n 1) ✓"
        fi
    fi
}

# Check Homebrew installation
check_homebrew() {
    print_header "Step 3: Checking Homebrew"
    
    if ! command -v brew &> /dev/null; then
        print_warning "Homebrew is not installed!"
        print_message "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        print_message "Homebrew installed successfully ✓"
    else
        print_message "Homebrew version: $(brew --version | head -n 1) ✓"
    fi
}

# Install Kafka
install_kafka() {
    print_header "Step 4: Installing Apache Kafka"
    
    if brew list kafka &> /dev/null; then
        print_warning "Kafka is already installed!"
        read -p "Do you want to reinstall? (y/n): " choice
        if [[ $choice == "y" || $choice == "Y" ]]; then
            print_message "Reinstalling Kafka..."
            brew reinstall kafka
        else
            print_message "Skipping Kafka installation"
        fi
    else
        print_message "Installing Kafka via Homebrew..."
        brew install kafka
        print_message "Kafka installed successfully ✓"
    fi
    
    # Get Kafka installation path
    KAFKA_HOME=$(brew --prefix kafka)
    print_message "Kafka installed at: $KAFKA_HOME"
}

# Configure Kafka
configure_kafka() {
    print_header "Step 5: Configuring Kafka"
    
    # Add Kafka commands to PATH
    if ! grep -q "kafka/bin" ~/.zshrc; then
        echo 'export PATH="/opt/homebrew/opt/kafka/bin:$PATH"' >> ~/.zshrc
        print_message "Added Kafka binaries to PATH ✓"
    fi
    
    source ~/.zshrc 2>/dev/null || true
    
    print_message "Configuration completed ✓"
}

# Initialize Kafka (KRaft mode)
initialize_kafka() {
    print_header "Step 6: Initializing Kafka (KRaft mode)"
    
    print_message "Generating Cluster UUID..."
    KAFKA_CLUSTER_ID=$(kafka-storage random-uuid)
    echo "Cluster UUID: $KAFKA_CLUSTER_ID"
    
    print_message "Formatting log directories..."
    # Use server.properties for Homebrew Kafka 4.1.0
    kafka-storage format -t $KAFKA_CLUSTER_ID -c /opt/homebrew/etc/kafka/server.properties
    
    print_message "Kafka initialized successfully ✓"
}

# Create startup script
create_startup_script() {
    print_header "Step 7: Creating Startup Scripts"
    
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Start Kafka script
    cat > "$SCRIPT_DIR/start-kafka.sh" << 'EOF'
#!/bin/bash
echo "Starting Apache Kafka..."
# Use server.properties (not kraft/server.properties for Homebrew 4.1.0)
kafka-server-start /opt/homebrew/etc/kafka/server.properties
EOF
    
    # Stop Kafka script
    cat > "$SCRIPT_DIR/stop-kafka.sh" << 'EOF'
#!/bin/bash
echo "Stopping Apache Kafka..."
pkill -f kafka.Kafka
echo "Kafka stopped."
EOF
    
    # Create topic script
    cat > "$SCRIPT_DIR/create-topic.sh" << 'EOF'
#!/bin/bash
TOPIC_NAME=${1:-"quickstart-events"}
echo "Creating topic: $TOPIC_NAME"
kafka-topics --create --topic $TOPIC_NAME --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
echo "Topic created successfully!"
EOF
    
    # List topics script
    cat > "$SCRIPT_DIR/list-topics.sh" << 'EOF'
#!/bin/bash
echo "Listing all Kafka topics..."
kafka-topics --list --bootstrap-server localhost:9092
EOF
    
    # Start producer script
    cat > "$SCRIPT_DIR/start-producer.sh" << 'EOF'
#!/bin/bash
TOPIC_NAME=${1:-"quickstart-events"}
echo "Starting Kafka Producer for topic: $TOPIC_NAME"
echo "Type your messages (Ctrl+C to exit):"
kafka-console-producer --topic $TOPIC_NAME --bootstrap-server localhost:9092
EOF
    
    # Start consumer script
    cat > "$SCRIPT_DIR/start-consumer.sh" << 'EOF'
#!/bin/bash
TOPIC_NAME=${1:-"quickstart-events"}
echo "Starting Kafka Consumer for topic: $TOPIC_NAME"
kafka-console-consumer --topic $TOPIC_NAME --from-beginning --bootstrap-server localhost:9092
EOF
    
    # Make scripts executable
    chmod +x "$SCRIPT_DIR"/*.sh
    
    print_message "Helper scripts created in: $SCRIPT_DIR"
    echo ""
    echo "  - start-kafka.sh     : Start Kafka server"
    echo "  - stop-kafka.sh      : Stop Kafka server"
    echo "  - create-topic.sh    : Create a topic"
    echo "  - list-topics.sh     : List all topics"
    echo "  - start-producer.sh  : Start producer console"
    echo "  - start-consumer.sh  : Start consumer console"
    echo ""
}

# Verify installation
verify_installation() {
    print_header "Step 8: Verifying Installation"
    
    # Check if Kafka commands are available
    if command -v kafka-topics &> /dev/null; then
        print_message "kafka-topics command: Available ✓"
    else
        print_error "kafka-topics command not found!"
    fi
    
    if command -v kafka-server-start &> /dev/null; then
        print_message "kafka-server-start command: Available ✓"
    else
        print_error "kafka-server-start command not found!"
    fi
    
    if command -v kafka-console-producer &> /dev/null; then
        print_message "kafka-console-producer command: Available ✓"
    else
        print_error "kafka-console-producer command not found!"
    fi
    
    if command -v kafka-console-consumer &> /dev/null; then
        print_message "kafka-console-consumer command: Available ✓"
    else
        print_error "kafka-console-consumer command not found!"
    fi
}

# Print next steps
print_next_steps() {
    print_header "Installation Complete! 🎉"
    
    echo -e "${GREEN}Kafka has been successfully installed on your Mac!${NC}\n"
    
    echo -e "${YELLOW}Next Steps:${NC}"
    echo ""
    echo "1. Start Kafka Server:"
    echo -e "   ${BLUE}./start-kafka.sh${NC}"
    echo ""
    echo "2. In a NEW terminal, create a topic:"
    echo -e "   ${BLUE}./create-topic.sh my-topic${NC}"
    echo ""
    echo "3. Start a Producer (in another terminal):"
    echo -e "   ${BLUE}./start-producer.sh my-topic${NC}"
    echo ""
    echo "4. Start a Consumer (in another terminal):"
    echo -e "   ${BLUE}./start-consumer.sh my-topic${NC}"
    echo ""
    echo "5. To list all topics:"
    echo -e "   ${BLUE}./list-topics.sh${NC}"
    echo ""
    echo "6. To stop Kafka:"
    echo -e "   ${BLUE}./stop-kafka.sh${NC}"
    echo ""
    echo -e "${YELLOW}Important Notes:${NC}"
    echo "- Restart your terminal or run: source ~/.zshrc"
    echo "- Kafka will run on port 9092 (default)"
    echo "- Logs location: /opt/homebrew/var/log/kafka/"
    echo ""
    echo -e "${GREEN}Happy Learning with Apache Kafka! 🚀${NC}"
    echo ""
}

# Main installation flow
main() {
    clear
    echo -e "${BLUE}"
    echo "╔════════════════════════════════════════╗"
    echo "║  Apache Kafka Installation Script     ║"
    echo "║  for macOS (Hinglish Edition)         ║"
    echo "╚════════════════════════════════════════╝"
    echo -e "${NC}"
    
    check_os
    check_homebrew
    check_java
    install_kafka
    configure_kafka
    initialize_kafka
    create_startup_script
    verify_installation
    print_next_steps
}

# Run main function
main
