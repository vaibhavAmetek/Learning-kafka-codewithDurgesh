#!/bin/bash

#################################################
# Kafka Data Pipeline Project - Setup Script
# One-click setup for the complete project
#################################################

echo "╔════════════════════════════════════════╗"
echo "║  Kafka Data Pipeline Setup Script     ║"
echo "║  Python → Kafka → Druid → Grafana     ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check Python
echo -e "${YELLOW}[1/4] Checking Python installation...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✅ Python found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}❌ Python 3 not found! Please install Python 3.8+${NC}"
    exit 1
fi

# Step 2: Check Kafka
echo -e "\n${YELLOW}[2/4] Checking Kafka status...${NC}"
if lsof -i :9092 &> /dev/null; then
    echo -e "${GREEN}✅ Kafka is running on port 9092${NC}"
else
    echo -e "${YELLOW}⚠️  Kafka is not running!${NC}"
    echo -e "${YELLOW}   Please start Kafka first:${NC}"
    echo -e "${YELLOW}   cd .. && ./start-kafka.sh${NC}"
    read -p "   Press Enter after starting Kafka..."
fi

# Step 3: Install Dependencies
echo -e "\n${YELLOW}[3/4] Installing Python dependencies...${NC}"
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Dependencies installed successfully${NC}"
    else
        echo -e "${RED}❌ Failed to install dependencies${NC}"
        exit 1
    fi
else
    echo -e "${RED}❌ requirements.txt not found!${NC}"
    exit 1
fi

# Step 4: Verify Setup
echo -e "\n${YELLOW}[4/4] Verifying setup...${NC}"

# Check confluent-kafka
if python3 -c "import confluent_kafka" 2>/dev/null; then
    echo -e "${GREEN}✅ confluent-kafka installed${NC}"
else
    echo -e "${RED}❌ confluent-kafka not found${NC}"
fi

# Check faker
if python3 -c "import faker" 2>/dev/null; then
    echo -e "${GREEN}✅ faker installed${NC}"
else
    echo -e "${YELLOW}⚠️  faker not installed (optional)${NC}"
fi

# Summary
echo -e "\n╔════════════════════════════════════════╗"
echo -e "║         Setup Complete! 🎉             ║"
echo -e "╚════════════════════════════════════════╝"
echo ""
echo -e "${GREEN}Next Steps:${NC}"
echo ""
echo "1. Quick Test (Recommended):"
echo "   python3 producer/simple_producer.py"
echo ""
echo "2. In another terminal:"
echo "   python3 consumer/simple_consumer.py"
echo ""
echo "3. Product Catalog:"
echo "   python3 producer/catalog_producer.py"
echo ""
echo -e "${YELLOW}📚 Documentation:${NC}"
echo "   - README.md - Project overview"
echo "   - docs/TASKS.md - All tasks explained"
echo "   - docs/SETUP_GUIDE.md - Detailed setup"
echo "   - docs/TROUBLESHOOTING.md - Common issues"
echo ""
echo -e "${GREEN}Happy Learning! 🚀${NC}"
