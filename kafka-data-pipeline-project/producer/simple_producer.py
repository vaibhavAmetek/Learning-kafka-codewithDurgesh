"""
Task 2: Simple Kafka Producer (Getting Started)
================================================
Ye sabse basic producer hai - "Hello World" type
Isse shuru karo Kafka seekhne ke liye

Kya karta hai:
- Kafka se connect hota hai
- Simple messages send karta hai
- Delivery confirmation deta hai

Author: Your Name
Date: November 24, 2024
"""

# ============================================
# IMPORTS - Required libraries
# ============================================

# Confluent Kafka library - main library for Kafka operations
from confluent_kafka import Producer

# JSON library - data ko JSON format mein convert karne ke liye
import json

# Time library - timestamps aur delays ke liye
import time

# Datetime - current date/time ke liye
from datetime import datetime

# Sys library - command line arguments aur exit ke liye
import sys

# Config file import karo - humne banaya hai
import sys
import os
# Parent directory ko path mein add karo taaki config import ho sake
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.kafka_config import get_producer_config, get_topic_name

# ============================================
# CALLBACK FUNCTION
# ============================================

def delivery_report(err, msg):
    """
    Ye function tab call hota hai jab message deliver ho jata hai (ya fail ho jata hai)
    
    Args:
        err: Error object (agar koi error hua to)
        msg: Message object (jo send kiya tha)
    
    Callback function ka matlab:
    - Jab message send karte ho, turant result nahi milta
    - Jab result aata hai, ye function automatically call hota hai
    - Isse pata chalta hai ki message successfully gaya ya nahi
    """
    if err is not None:
        # Agar error hai to print karo
        print(f'❌ Message delivery FAILED: {err}')
    else:
        # Success! Message deliver ho gaya
        print(f'✅ Message delivered to {msg.topic()} [partition {msg.partition()}] at offset {msg.offset()}')
        # Topic: Kis topic mein gaya
        # Partition: Kis partition mein store hua
        # Offset: Partition mein kis position pe hai


# ============================================
# PRODUCER CLASS
# ============================================

class SimpleProducer:
    """
    Simple Kafka Producer class
    
    Ye class Kafka producer ko manage karti hai
    Object-oriented approach - professional way
    """
    
    def __init__(self):
        """
        Constructor - jab object banate ho tab ye run hota hai
        Producer initialize karta hai
        """
        print("🚀 Initializing Simple Kafka Producer...")
        
        # Config file se settings le aao
        self.config = get_producer_config()
        
        # Producer object banao
        # Ye actual Kafka se connection banata hai
        try:
            self.producer = Producer(self.config)
            print(f"✅ Connected to Kafka at {self.config['bootstrap.servers']}")
        except Exception as e:
            print(f"❌ Failed to create producer: {e}")
            sys.exit(1)
        
        # Topic name config se le lo
        self.topic = get_topic_name('test')
        print(f"📝 Using topic: {self.topic}")
    
    
    def send_message(self, message_data):
        """
        Kafka mein message send karta hai
        
        Args:
            message_data (dict): Jo data send karna hai (dictionary format mein)
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Dictionary ko JSON string mein convert karo
            # Kafka mein string/bytes format mein data jaata hai
            message_json = json.dumps(message_data)
            
            # Message send karo
            self.producer.produce(
                topic=self.topic,              # Kis topic mein bhejni hai
                value=message_json,            # Actual message (JSON string)
                callback=delivery_report       # Callback function (result ke liye)
            )
            
            # Poll karo - ye callbacks ko trigger karta hai
            # 0 = non-blocking, turant return ho jayega
            self.producer.poll(0)
            
            return True
            
        except Exception as e:
            print(f"❌ Error sending message: {e}")
            return False
    
    
    def send_multiple_messages(self, count=5):
        """
        Multiple messages send karta hai - testing ke liye
        
        Args:
            count (int): Kitne messages send karne hain
        """
        print(f"\n📤 Sending {count} messages to Kafka...")
        
        for i in range(count):
            # Message data prepare karo
            message = {
                'message_id': i + 1,
                'text': f'Hello from Kafka! Message #{i + 1}',
                'timestamp': datetime.now().isoformat(),
                'sender': 'SimpleProducer'
            }
            
            print(f"\n📨 Sending message {i + 1}/{count}:")
            print(f"   Data: {message}")
            
            # Message send karo
            self.send_message(message)
            
            # Thoda wait karo - messages ko space do
            time.sleep(1)
        
        # Saare pending messages ko flush karo
        # Flush = wait karo jab tak saare messages send na ho jaye
        print("\n⏳ Flushing producer (waiting for all messages to be sent)...")
        self.producer.flush()
        print("✅ All messages sent successfully!")
    
    
    def send_custom_message(self, text):
        """
        Custom text message send karta hai
        
        Args:
            text (str): Jo message bhejna hai
        """
        message = {
            'text': text,
            'timestamp': datetime.now().isoformat(),
            'sender': 'SimpleProducer'
        }
        
        print(f"\n📨 Sending custom message: {text}")
        self.send_message(message)
        self.producer.flush()
    
    
    def close(self):
        """
        Producer ko properly close karta hai
        Ye important hai - resources free karne ke liye
        """
        print("\n🔒 Closing producer...")
        self.producer.flush()  # Pending messages send karo
        print("✅ Producer closed successfully!")


# ============================================
# INTERACTIVE MODE
# ============================================

def interactive_mode():
    """
    Interactive mode - user se input le ke messages send karo
    """
    print("\n" + "="*50)
    print("🎮 INTERACTIVE MODE")
    print("="*50)
    print("Type your messages and press Enter to send")
    print("Type 'quit' or 'exit' to stop")
    print("="*50 + "\n")
    
    # Producer object banao
    producer = SimpleProducer()
    
    try:
        while True:
            # User se input lo
            user_input = input("💬 Enter message: ").strip()
            
            # Exit conditions check karo
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Exiting interactive mode...")
                break
            
            # Empty message check karo
            if not user_input:
                print("⚠️  Empty message! Please type something.")
                continue
            
            # Message send karo
            producer.send_custom_message(user_input)
            print("✅ Message sent!\n")
    
    except KeyboardInterrupt:
        # Ctrl+C press kiya to gracefully exit karo
        print("\n\n⚠️  Interrupted by user (Ctrl+C)")
    
    finally:
        # Producer ko close karo (always)
        producer.close()


# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """
    Main function - program yaha se start hota hai
    """
    print("\n" + "="*50)
    print("🚀 SIMPLE KAFKA PRODUCER - TASK 2")
    print("="*50)
    
    # Producer object banao
    producer = SimpleProducer()
    
    try:
        # 5 test messages send karo
        producer.send_multiple_messages(count=5)
        
        # User ko option do - interactive mode chahiye?
        print("\n" + "="*50)
        choice = input("\n🤔 Want to send custom messages? (y/n): ").strip().lower()
        
        if choice == 'y':
            producer.close()  # Pehle wala close karo
            interactive_mode()  # Interactive mode start karo
        else:
            print("👍 Okay, exiting...")
            producer.close()
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Program interrupted by user (Ctrl+C)")
        producer.close()
    
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        producer.close()
        sys.exit(1)
    
    print("\n✅ Program completed successfully!")
    print("="*50 + "\n")


# ============================================
# PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    """
    Ye check karta hai ki file directly run ho rahi hai ya import ho rahi hai
    Agar directly run ho rahi hai to main() function call hoga
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

2. Run this producer:
   python producer/simple_producer.py

3. In another terminal, run consumer to see messages:
   python consumer/simple_consumer.py


WHAT YOU'LL SEE:
----------------
- Producer connecting to Kafka
- 5 test messages being sent
- Delivery confirmations
- Option for interactive mode


TROUBLESHOOTING:
----------------
- If connection fails: Check if Kafka is running (lsof -i :9092)
- If topic not found: It will be auto-created
- If messages not visible: Run consumer in another terminal


NEXT STEPS:
-----------
1. Run this producer
2. Run simple_consumer.py to see messages
3. Try interactive mode
4. Modify message structure
5. Move to catalog_producer.py (Task 1)
"""
