#!/bin/bash

# 🚀 Create iTerm2 Multi-Pane Layout for Kafka
# This creates 4 panes: Zookeeper, Kafka, Producer, Consumer

echo "🚀 Creating Kafka development layout in iTerm2..."

osascript <<APPLESCRIPT
tell application "iTerm"
    activate
    
    -- Create new window
    create window with default profile
    
    tell current session of current window
        -- Pane 1: Zookeeper
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "clear"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo '🐘 ZOOKEEPER SERVER'"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo ''"
        write text "echo '📍 Port: 2181'"
        write text "echo '📝 Config: /opt/homebrew/etc/kafka/zookeeper.properties'"
        write text "echo ''"
        write text "echo '▶️  To start:'"
        write text "echo '   zookeeper-server-start /opt/homebrew/etc/kafka/zookeeper.properties'"
        write text "echo ''"
        
        -- Split horizontally for Kafka
        split horizontally with default profile
    end tell
    
    tell second session of current tab of current window
        -- Pane 2: Kafka Server
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "clear"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo '🚀 KAFKA SERVER'"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo ''"
        write text "echo '📍 Port: 9092'"
        write text "echo '📝 Config: /opt/homebrew/etc/kafka/broker.properties'"
        write text "echo ''"
        write text "echo '⚠️  Start Zookeeper first (Pane 1)!'"
        write text "echo ''"
        write text "echo '▶️  To start:'"
        write text "echo '   kafka-server-start /opt/homebrew/etc/kafka/broker.properties'"
        write text "echo ''"
        
        -- Split vertically for Producer
        split vertically with default profile
    end tell
    
    tell third session of current tab of current window
        -- Pane 3: Producer
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "clear"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo '📤 KAFKA PRODUCER'"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo ''"
        write text "echo '📝 Send messages to Kafka topics'"
        write text "echo ''"
        write text "echo '▶️  Quick start:'"
        write text "echo '   # Create topic'"
        write text "echo '   kafka-topics --create --topic test --bootstrap-server localhost:9092'"
        write text "echo ''"
        write text "echo '   # Start producer'"
        write text "echo '   kafka-console-producer --topic test --bootstrap-server localhost:9092'"
        write text "echo ''"
        write text "echo '💡 Type messages and press Enter to send'"
        write text "echo ''"
    end tell
    
    tell second session of current tab of current window
        -- Split vertically for Consumer
        split vertically with default profile
    end tell
    
    tell fourth session of current tab of current window
        -- Pane 4: Consumer
        write text "cd ~/Projects/Learning-kafka-codewithDurgesh"
        write text "clear"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo '📥 KAFKA CONSUMER'"
        write text "echo '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'"
        write text "echo ''"
        write text "echo '📝 Receive messages from Kafka topics'"
        write text "echo ''"
        write text "echo '▶️  To start:'"
        write text "echo '   kafka-console-consumer --topic test --from-beginning --bootstrap-server localhost:9092'"
        write text "echo ''"
        write text "echo '💡 Messages will appear here in real-time'"
        write text "echo ''"
    end tell
    
end tell
APPLESCRIPT

echo "✅ Layout created!"
echo ""
echo "📋 Pane Layout:"
echo "┌─────────────────────────────────────┐"
echo "│  Pane 1: Zookeeper (Port 2181)     │"
echo "├─────────────────────────────────────┤"
echo "│  Pane 2: Kafka Server (Port 9092)  │"
echo "├──────────────────┬──────────────────┤"
echo "│  Pane 3:         │  Pane 4:         │"
echo "│  Producer        │  Consumer        │"
echo "└──────────────────┴──────────────────┘"
echo ""
echo "🎯 Next Steps:"
echo "1. Start Zookeeper (Pane 1)"
echo "2. Start Kafka (Pane 2)"
echo "3. Create topic & produce (Pane 3)"
echo "4. Consume messages (Pane 4)"
echo ""
echo "📖 Commands guide: Kafka_Console_Commands.md"
