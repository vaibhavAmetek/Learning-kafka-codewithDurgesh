"""
Task 1: Product Catalog Producer
=================================
Ye producer product catalog banata hai aur Kafka mein send karta hai
Real-world e-commerce example - Flipkart/Amazon jaisa

Kya karta hai:
- Product data generate karta hai (realistic data)
- Kafka mein send karta hai
- Batch processing support karta hai

Author: Your Name
Date: November 24, 2024
"""

# ============================================
# IMPORTS
# ============================================

from confluent_kafka import Producer
import json
import time
from datetime import datetime
import sys
import os
import random

# Faker library - realistic fake data generate karne ke liye
try:
    from faker import Faker
    FAKER_AVAILABLE = True
except ImportError:
    print("⚠️  Faker library not installed. Using basic data generation.")
    print("   Install with: pip install faker")
    FAKER_AVAILABLE = False

# Config import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.kafka_config import get_producer_config, get_topic_name

# ============================================
# PRODUCT DATA GENERATOR
# ============================================

class ProductGenerator:
    """
    Product data generate karta hai - realistic aur random
    """
    
    def __init__(self):
        """Initialize product generator"""
        if FAKER_AVAILABLE:
            self.faker = Faker()
        
        # Product categories - real e-commerce categories
        self.categories = [
            'Electronics', 'Clothing', 'Books', 'Home & Kitchen',
            'Sports', 'Toys', 'Beauty', 'Automotive', 'Grocery', 'Health'
        ]
        
        # Product name templates - category wise
        self.product_templates = {
            'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Smart Watch', 'Tablet', 'Camera'],
            'Clothing': ['T-Shirt', 'Jeans', 'Jacket', 'Shoes', 'Dress', 'Sweater'],
            'Books': ['Novel', 'Textbook', 'Comic', 'Magazine', 'Biography', 'Self-Help'],
            'Home & Kitchen': ['Mixer', 'Microwave', 'Cookware Set', 'Dinner Set', 'Bedsheet', 'Curtains'],
            'Sports': ['Cricket Bat', 'Football', 'Yoga Mat', 'Dumbbells', 'Bicycle', 'Tennis Racket'],
            'Toys': ['Action Figure', 'Puzzle', 'Board Game', 'Doll', 'Remote Car', 'Building Blocks'],
            'Beauty': ['Face Cream', 'Lipstick', 'Perfume', 'Shampoo', 'Face Wash', 'Hair Oil'],
            'Automotive': ['Car Cover', 'Seat Covers', 'Air Freshener', 'Toolkit', 'Polish', 'Cleaner'],
            'Grocery': ['Rice', 'Dal', 'Oil', 'Flour', 'Sugar', 'Tea', 'Coffee'],
            'Health': ['Vitamins', 'Protein Powder', 'First Aid Kit', 'Thermometer', 'BP Monitor']
        }
        
        # Brands - category wise
        self.brands = {
            'Electronics': ['Samsung', 'Apple', 'Sony', 'LG', 'OnePlus', 'Xiaomi'],
            'Clothing': ['Nike', 'Adidas', 'Puma', 'Levi\'s', 'Zara', 'H&M'],
            'Books': ['Penguin', 'HarperCollins', 'Scholastic', 'Oxford', 'McGraw Hill'],
            'Home & Kitchen': ['Prestige', 'Hawkins', 'Milton', 'Cello', 'Borosil'],
            'Sports': ['Nivia', 'Cosco', 'Yonex', 'Decathlon', 'Reebok'],
            'Toys': ['Hasbro', 'Mattel', 'LEGO', 'Fisher-Price', 'Funskool'],
            'Beauty': ['Lakme', 'Maybelline', 'L\'Oreal', 'Nivea', 'Dove'],
            'Automotive': ['3M', 'Bosch', 'Philips', 'Michelin'],
            'Grocery': ['Tata', 'Aashirvaad', 'Fortune', 'India Gate', 'Amul'],
            'Health': ['Himalaya', 'Dabur', 'Patanjali', 'Baidyanath']
        }
    
    
    def generate_product(self, product_id=None):
        """
        Ek product ka data generate karta hai
        
        Args:
            product_id (str, optional): Custom product ID
        
        Returns:
            dict: Product data
        """
        # Random category select karo
        category = random.choice(self.categories)
        
        # Category ke according product aur brand select karo
        product_type = random.choice(self.product_templates.get(category, ['Product']))
        brand = random.choice(self.brands.get(category, ['Generic']))
        
        # Product ID generate karo
        if not product_id:
            product_id = f"P{random.randint(10000, 99999)}"
        
        # Price generate karo - category ke according
        price_ranges = {
            'Electronics': (5000, 100000),
            'Clothing': (500, 5000),
            'Books': (100, 1000),
            'Home & Kitchen': (500, 10000),
            'Sports': (500, 5000),
            'Toys': (200, 3000),
            'Beauty': (100, 2000),
            'Automotive': (200, 5000),
            'Grocery': (50, 500),
            'Health': (100, 2000)
        }
        
        min_price, max_price = price_ranges.get(category, (100, 1000))
        price = random.randint(min_price, max_price)
        
        # Stock quantity - random
        stock = random.randint(0, 500)
        
        # Rating - 1 to 5 stars
        rating = round(random.uniform(2.5, 5.0), 1)
        
        # Reviews count
        reviews = random.randint(0, 10000)
        
        # Discount percentage
        discount = random.choice([0, 5, 10, 15, 20, 25, 30, 40, 50])
        
        # Product data dictionary
        product = {
            'product_id': product_id,
            'name': f"{brand} {product_type}",
            'category': category,
            'brand': brand,
            'price': price,
            'discount_percent': discount,
            'final_price': int(price * (1 - discount/100)),
            'stock': stock,
            'in_stock': stock > 0,
            'rating': rating,
            'reviews_count': reviews,
            'timestamp': datetime.now().isoformat(),
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return product
    
    
    def generate_catalog(self, count=10):
        """
        Multiple products ka catalog generate karta hai
        
        Args:
            count (int): Kitne products generate karne hain
        
        Returns:
            list: Products ki list
        """
        catalog = []
        for i in range(count):
            product = self.generate_product()
            catalog.append(product)
        return catalog


# ============================================
# CATALOG PRODUCER CLASS
# ============================================

class CatalogProducer:
    """
    Product catalog ko Kafka mein send karta hai
    """
    
    def __init__(self):
        """Initialize catalog producer"""
        print("🚀 Initializing Product Catalog Producer...")
        
        # Config aur producer setup
        self.config = get_producer_config()
        self.producer = Producer(self.config)
        self.topic = get_topic_name('products')
        
        # Product generator initialize karo
        self.generator = ProductGenerator()
        
        print(f"✅ Connected to Kafka at {self.config['bootstrap.servers']}")
        print(f"📝 Using topic: {self.topic}")
    
    
    def delivery_callback(self, err, msg):
        """
        Delivery confirmation callback
        """
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            # Success message - compact format
            product_id = json.loads(msg.value().decode('utf-8'))['product_id']
            print(f"✅ Product {product_id} → partition {msg.partition()}, offset {msg.offset()}")
    
    
    def send_product(self, product_data):
        """
        Ek product ko Kafka mein send karta hai
        
        Args:
            product_data (dict): Product ka data
        
        Returns:
            bool: Success/failure
        """
        try:
            # JSON mein convert karo
            message = json.dumps(product_data)
            
            # Product ID ko key ki tarah use karo
            # Key se same product hamesha same partition mein jayega
            key = product_data['product_id']
            
            # Kafka mein send karo
            self.producer.produce(
                topic=self.topic,
                key=key,
                value=message,
                callback=self.delivery_callback
            )
            
            # Poll to trigger callbacks
            self.producer.poll(0)
            
            return True
            
        except Exception as e:
            print(f"❌ Error sending product: {e}")
            return False
    
    
    def send_catalog(self, count=10, delay=0.5):
        """
        Complete catalog send karta hai
        
        Args:
            count (int): Kitne products send karne hain
            delay (float): Products ke beech mein delay (seconds)
        """
        print(f"\n{'='*60}")
        print(f"📦 SENDING PRODUCT CATALOG TO KAFKA")
        print(f"{'='*60}")
        print(f"Products to send: {count}")
        print(f"Topic: {self.topic}")
        print(f"Delay between products: {delay}s")
        print(f"{'='*60}\n")
        
        # Catalog generate karo
        catalog = self.generator.generate_catalog(count)
        
        # Har product ko send karo
        success_count = 0
        for i, product in enumerate(catalog, 1):
            print(f"\n📤 [{i}/{count}] Sending: {product['name']}")
            print(f"   Category: {product['category']} | Price: ₹{product['final_price']} | Stock: {product['stock']}")
            
            if self.send_product(product):
                success_count += 1
            
            # Delay (agar last product nahi hai)
            if i < count:
                time.sleep(delay)
        
        # Flush - saare messages send ho jane ka wait karo
        print(f"\n⏳ Flushing producer...")
        self.producer.flush()
        
        # Summary
        print(f"\n{'='*60}")
        print(f"📊 SUMMARY")
        print(f"{'='*60}")
        print(f"✅ Successfully sent: {success_count}/{count} products")
        print(f"❌ Failed: {count - success_count}")
        print(f"{'='*60}\n")
    
    
    def send_continuous(self, interval=5):
        """
        Continuous mode - har interval pe naye products send karo
        Real-time streaming simulation
        
        Args:
            interval (int): Seconds mein interval
        """
        print(f"\n{'='*60}")
        print(f"🔄 CONTINUOUS STREAMING MODE")
        print(f"{'='*60}")
        print(f"Sending 1 product every {interval} seconds")
        print(f"Press Ctrl+C to stop")
        print(f"{'='*60}\n")
        
        count = 0
        try:
            while True:
                count += 1
                product = self.generator.generate_product()
                
                print(f"\n📤 [{count}] {product['name']} → Kafka")
                self.send_product(product)
                
                time.sleep(interval)
                
        except KeyboardInterrupt:
            print(f"\n\n⚠️  Stopped by user (Ctrl+C)")
            print(f"📊 Total products sent: {count}")
        
        finally:
            self.close()
    
    
    def close(self):
        """Close producer properly"""
        print("\n🔒 Closing producer...")
        self.producer.flush()
        print("✅ Producer closed!")


# ============================================
# MAIN FUNCTION
# ============================================

def main():
    """Main function"""
    print("\n" + "="*60)
    print("🛍️  PRODUCT CATALOG PRODUCER - TASK 1")
    print("="*60)
    
    # Producer banao
    producer = CatalogProducer()
    
    # Menu dikhao
    print("\n🎯 Choose mode:")
    print("   1. Send batch of products (one-time)")
    print("   2. Continuous streaming (real-time)")
    print("   3. Quick test (5 products)")
    
    choice = input("\nYour choice (1/2/3): ").strip()
    
    try:
        if choice == '1':
            # Batch mode
            count = input("How many products to send? (default 10): ").strip()
            count = int(count) if count.isdigit() else 10
            producer.send_catalog(count=count)
            producer.close()
            
        elif choice == '2':
            # Continuous mode
            interval = input("Interval in seconds? (default 5): ").strip()
            interval = int(interval) if interval.isdigit() else 5
            producer.send_continuous(interval=interval)
            
        elif choice == '3':
            # Quick test
            print("\n🚀 Quick test mode - sending 5 products")
            producer.send_catalog(count=5, delay=1)
            producer.close()
            
        else:
            print("❌ Invalid choice!")
            producer.close()
            return
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        producer.close()
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        producer.close()
        sys.exit(1)
    
    print("\n✅ Program completed!")
    print("="*60 + "\n")


# ============================================
# ENTRY POINT
# ============================================

if __name__ == "__main__":
    main()


# ============================================
# USAGE EXAMPLES
# ============================================

"""
HOW TO RUN:
-----------

1. Start Kafka:
   cd ..
   ./start-kafka.sh

2. Run this producer:
   python producer/catalog_producer.py

3. Choose mode and follow prompts

4. In another terminal, run consumer:
   python consumer/simple_consumer.py


WHAT IT DOES:
-------------
- Generates realistic product data
- Sends to Kafka topic 'product-catalog'
- Supports batch and streaming modes
- Uses product_id as message key


SAMPLE OUTPUT:
--------------
Product: Samsung Smartphone
Category: Electronics
Price: ₹45,000
Stock: 150
Rating: 4.5 ⭐


NEXT STEPS:
-----------
1. Run this producer
2. See products being sent
3. Run consumer to verify
4. Try continuous mode
5. Modify product templates
6. Add more categories
"""
