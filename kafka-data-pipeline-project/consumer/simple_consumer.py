"""
Task 2: Simple Kafka Consumer (Getting Started)
================================================
Ye basic consumer hai jo messages receive karta hai
Producer ke saath use karo - messages dekhne ke liye

Kya karta hai:
- Kafka se connect hota hai
- Messages receive karta hai
- Console mein print karta hai

Author: Your Name
Date: November 24, 2024
"""

# ============================================
# IMPORTS - Required libraries
# ============================================

from confluent_kafka import Consumer, KafkaError, KafkaException
import json
import sys
import os

# Config file import karo
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.kafka_config import get_consumer_config, get_topic_name

# ============================================
# CONSUMER CLASS
# ============================================

class SimpleConsumer:
    """
    Simple Kafka Consumer class
    Messages receive karta hai aur print karta hai
    """
    
    def __init__(self):
        """
        Constructor - Consumer initialize karta hai
        """
        print("🚀 Initializing Simple Kafka Consumer...")
        
        # Config file se settings le aao
        self.config = get_consumer_config()
        
        # Consumer object banao
        try:
            self.consumer = Consumer(self.config)
            print(f"✅ Connected to Kafka at {self.config['bootstrap.servers']}")
        except Exception as e:
            print(f"❌ Failed to create consumer: {e}")
            sys.exit(1)
        
        # Topic name config se le lo
        self.topic = get_topic_name('test')
        
        # Topic ko subscribe karo
        # Subscribe ka matlab: is topic ke messages chahiye
        self.consumer.subscribe([self.topic])
        print(f"📝 Subscribed to topic: {self.topic}")
        print(f"👥 Consumer group: {self.config['group.id']}")
    
    
    def consume_messages(self, max_messages=None):
        """
        Messages consume karta hai aur print karta hai
        
        Args:
            max_messages (int, optional): Kitne messages receive karne hain
                                         None = infinite (Ctrl+C se stop karo)
        """
        print("\n" + "="*50)
        print("📥 CONSUMING MESSAGES")
        print("="*50)
        print("Waiting for messages... (Press Ctrl+C to stop)")
        print("="*50 + "\n")
        
        message_count = 0
        
        try:
            while True:
                # Message poll karo (receive karo)
                # timeout=1.0 = 1 second wait karo message ke liye
                msg = self.consumer.poll(timeout=1.0)
                
                # Agar koi message nahi mila
                if msg is None:
                    # Timeout ho gaya, koi message nahi aaya
                    # Ye normal hai - continue karo
                    continue
                
                # Check karo agar error hai
                if msg.error():
                    # Error handle karo
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition - ye normal hai
                        # Matlab saare messages pad liye
                        print(f"📍 Reached end of partition {msg.partition()}")
                    else:
                        # Koi aur error hai
                        raise KafkaException(msg.error())
                else:
                    # Message successfully receive hua!
                    message_count += 1
                    
                    # Message ko process karo
                    self.process_message(msg, message_count)
                    
                    # Agar max_messages set hai aur reach kar gaye
                    if max_messages and message_count >= max_messages:
                        print(f"\n✅ Received {max_messages} messages. Stopping...")
                        break
        
        except KeyboardInterrupt:
            # User ne Ctrl+C press kiya
            print("\n\n⚠️  Interrupted by user (Ctrl+C)")
        
        finally:
            # Consumer ko close karo
            print(f"\n📊 Total messages received: {message_count}")
            self.close()
    
    
    def process_message(self, msg, count):
        """
        Individual message ko process karta hai
        
        Args:
            msg: Kafka message object
            count (int): Message number (counting ke liye)
        """
        # Message value ko decode karo (bytes se string)
        message_value = msg.value().decode('utf-8')
        
        # JSON string ko Python dictionary mein convert karo
        try:
            message_data = json.loads(message_value)
        except json.JSONDecodeError:
            # Agar JSON nahi hai to raw string hi use karo
            message_data = message_value
        
        # Message details print karo
        print(f"\n{'='*50}")
        print(f"📨 MESSAGE #{count}")
        print(f"{'='*50}")
        print(f"📍 Topic: {msg.topic()}")
        print(f"📦 Partition: {msg.partition()}")
        print(f"📌 Offset: {msg.offset()}")
        print(f"🔑 Key: {msg.key().decode('utf-8') if msg.key() else 'None'}")
        print(f"📝 Value:")
        
        # Pretty print karo (readable format mein)
        if isinstance(message_data, dict):
            # Dictionary hai to formatted print karo
            for key, value in message_data.items():
                print(f"   {key}: {value}")
        else:
            # String hai to directly print karo
            print(f"   {message_data}")
        
        print(f"{'='*50}")
    
    
    def close(self):
        """
        Consumer ko properly close karta hai
        """
        print("\n🔒 Closing consumer...")
        self.consumer.close()
        print("✅ Consumer closed successfully!")


# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """
    Main function - program yaha se start hota hai
    """
    print("\n" + "="*50)
    print("🚀 SIMPLE KAFKA CONSUMER - TASK 2")
    print("="*50)
    
    # Consumer object banao
    consumer = SimpleConsumer()
    
    # User ko option do
    print("\n🤔 How many messages do you want to receive?")
    print("   1. Enter a number (e.g., 5)")
    print("   2. Press Enter for infinite (stop with Ctrl+C)")
    
    choice = input("\nYour choice: ").strip()
    
    if choice.isdigit():
        # Number diya hai
        max_messages = int(choice)
        print(f"\n📥 Will receive {max_messages} messages")
        consumer.consume_messages(max_messages=max_messages)
    else:
        # Infinite mode
        print("\n📥 Receiving messages infinitely (Ctrl+C to stop)")
        consumer.consume_messages()
    
    print("\n✅ Program completed successfully!")
    print("="*50 + "\n")


# ============================================
# PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    """
    File directly run ho rahi hai to main() call karo
    """
    main()


# ============================================
# USAGE EXAMPLES
# ============================================

"""
HOW TO RUN:
-----------

1. Make sure Kafka is running:
   cd ..
   ./start-kafka.sh

2. Start producer in one terminal:
   python producer/simple_producer.py

3. Start this consumer in another terminal:
   python consumer/simple_consumer.py


WHAT YOU'LL SEE:
----------------
- Consumer connecting to Kafka
- Subscribing to topic
- Messages appearing in real-time
- Message details (topic, partition, offset)
- Message content (formatted)


CONSUMER GROUPS:
----------------
- Same group ke multiple consumers = Load balancing
  (Messages divide ho jayenge)
  
- Different group ke consumers = All get same messages
  (Sabko saare messages milenge)

Example:
Terminal 1: python consumer/simple_consumer.py  (group: default)
Terminal 2: python consumer/simple_consumer.py  (group: default)
→ Messages divide honge

To change group, modify config/kafka_config.py


TROUBLESHOOTING:
----------------
- No messages appearing: Check if producer is running
- Connection error: Check if Kafka is running (lsof -i :9092)
- Old messages appearing: Normal! Consumer reads from beginning
  (auto.offset.reset = 'earliest' in config)


NEXT STEPS:
-----------
1. Run producer and consumer together
2. See messages flowing in real-time
3. Try stopping and restarting consumer
4. Experiment with multiple consumers
5. Move to catalog_producer.py and catalog_consumer.py
"""
