"""
Kafka Configuration File
========================
Ye file mein saari Kafka settings hain
Isko import karke use karo - baar baar likhne ki zaroorat nahi

Author: Your Name
Date: November 24, 2024
"""

# ============================================
# KAFKA BROKER CONFIGURATION
# ============================================

# Kafka server ka address - yaha Kafka run ho raha hai
# localhost:9092 - local machine pe default port
BOOTSTRAP_SERVERS = 'localhost:9092'

# ============================================
# PRODUCER CONFIGURATION
# ============================================

# Producer ke liye settings
PRODUCER_CONFIG = {
    # Kafka server ka address
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    
    # Producer ka naam - debugging mein help karta hai
    'client.id': 'python-data-pipeline-producer',
    
    # Acknowledgment setting - kitna guarantee chahiye
    # 'all' = sabse safe, message definitely deliver hoga
    # '1' = leader broker ne receive kar liya (medium safe)
    # '0' = send and forget (fast but risky)
    'acks': 'all',
    
    # Agar message fail ho jaye to kitni baar retry kare
    'retries': 3,
    
    # Retry ke beech mein kitna wait kare (milliseconds)
    'retry.backoff.ms': 1000,
    
    # Message ordering guarantee ke liye
    # 1 = messages order mein rahenge
    'max.in.flight.requests.per.connection': 1,
    
    # Compression - data ko compress karke bhejo (bandwidth bachao)
    # Options: 'none', 'gzip', 'snappy', 'lz4', 'zstd'
    'compression.type': 'snappy',
    
    # Request timeout - kitni der wait kare response ka
    'request.timeout.ms': 30000,  # 30 seconds
}

# ============================================
# CONSUMER CONFIGURATION
# ============================================

# Consumer ke liye settings
CONSUMER_CONFIG = {
    # Kafka server ka address
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    
    # Consumer group ka naam
    # Same group ke consumers load balance karte hain
    # Different group ke consumers sabko same data milta hai
    'group.id': 'python-data-pipeline-consumer-group',
    
    # Consumer ka unique ID
    'client.id': 'python-data-pipeline-consumer',
    
    # Offset reset strategy
    # 'earliest' = topic ke start se padho (purane messages bhi)
    # 'latest' = sirf naye messages padho
    'auto.offset.reset': 'earliest',
    
    # Automatic offset commit
    # True = automatically commit hoga (easy but less control)
    # False = manually commit karna padega (more control)
    'enable.auto.commit': True,
    
    # Kitni der baad auto commit hoga (milliseconds)
    'auto.commit.interval.ms': 5000,  # 5 seconds
    
    # Session timeout - consumer alive hai ya nahi check karne ke liye
    'session.timeout.ms': 10000,  # 10 seconds
    
    # Maximum poll interval - kitni der tak poll nahi kiya to dead consider karo
    'max.poll.interval.ms': 300000,  # 5 minutes
}

# ============================================
# TOPIC NAMES
# ============================================

# Saare topics ke naam ek jagah
# Isse typo mistakes nahi hongi
TOPICS = {
    # Task 1: Product catalog topic
    'products': 'product-catalog',
    
    # Task 2: Simple test topic
    'test': 'test-topic',
    
    # Additional topics for real-world scenarios
    'orders': 'order-events',
    'deliveries': 'delivery-tracking',
    'analytics': 'analytics-events',
}

# ============================================
# TOPIC CONFIGURATIONS
# ============================================

# Topic create karte waqt ye settings use karo
TOPIC_CONFIG = {
    # Partitions - parallel processing ke liye
    # Zyada partitions = zyada parallelism
    'num_partitions': 3,
    
    # Replication factor - data backup ke liye
    # Production mein 3 recommended hai
    # Development mein 1 chalega
    'replication_factor': 1,
    
    # Retention time - kitni der tak messages store rahenge
    # -1 = forever, 86400000 = 1 day (in milliseconds)
    'retention_ms': 86400000,  # 1 day
}

# ============================================
# HELPER FUNCTIONS
# ============================================

def get_producer_config():
    """
    Producer configuration return karta hai
    
    Returns:
        dict: Producer ke liye configuration dictionary
    
    Example:
        config = get_producer_config()
        producer = Producer(config)
    """
    return PRODUCER_CONFIG.copy()  # Copy isliye ki original change na ho


def get_consumer_config(group_id=None):
    """
    Consumer configuration return karta hai
    
    Args:
        group_id (str, optional): Custom consumer group ID
    
    Returns:
        dict: Consumer ke liye configuration dictionary
    
    Example:
        config = get_consumer_config('my-custom-group')
        consumer = Consumer(config)
    """
    config = CONSUMER_CONFIG.copy()
    
    # Agar custom group_id di hai to use karo
    if group_id:
        config['group.id'] = group_id
    
    return config


def get_topic_name(topic_key):
    """
    Topic key se actual topic name return karta hai
    
    Args:
        topic_key (str): Topic ka key (e.g., 'products', 'orders')
    
    Returns:
        str: Actual topic name
    
    Example:
        topic = get_topic_name('products')
        # Returns: 'product-catalog'
    """
    return TOPICS.get(topic_key, topic_key)


def print_config():
    """
    Saari configuration print karta hai - debugging ke liye useful
    """
    print("=" * 50)
    print("KAFKA CONFIGURATION")
    print("=" * 50)
    print(f"\nBootstrap Servers: {BOOTSTRAP_SERVERS}")
    print(f"\nTopics:")
    for key, value in TOPICS.items():
        print(f"  {key}: {value}")
    print(f"\nProducer Config:")
    for key, value in PRODUCER_CONFIG.items():
        print(f"  {key}: {value}")
    print(f"\nConsumer Config:")
    for key, value in CONSUMER_CONFIG.items():
        print(f"  {key}: {value}")
    print("=" * 50)


# ============================================
# MAIN - Testing ke liye
# ============================================

if __name__ == "__main__":
    # Agar ye file directly run karo to config print hoga
    print("Kafka Configuration File")
    print("Ye file ko import karke use karo\n")
    print_config()
