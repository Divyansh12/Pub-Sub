# Python Pub/Sub System

A simple implementation of a Publisher-Subscriber (Pub/Sub) messaging pattern in Python. This system allows for decoupled communication between publishers and subscribers through topics.

## System Architecture

### Core Components

#### Models
- `models/subscriber.py`: Defines the Subscriber class that represents message consumers
  - `__init__(self, id)`: Initializes subscriber with unique ID
  - `get_id()`: Returns subscriber's unique identifier

- `models/topic.py`: Implements Topic class to manage message queues and subscriptions
  - `__init__(self, name)`: Creates topic with given name
  - `add_message(message)`: Adds message to topic's queue
  - `get_messages()`: Returns all messages in topic
  - `get_last_message()`: Returns most recent message
  - `add_subscriber(subscriber)`: Adds subscriber to topic
  - `remove_subscriber(subscriber)`: Removes subscriber from topic

- `models/publisher.py`: Contains Singleton Publisher class for message producers
  - `__new__(cls)`: Ensures single publisher instance
  - `__init__()`: Initializes publisher
  - `publish(message, topic)`: Publishes message to specific topic
  - `publish_to_all(message)`: Publishes message to all available topics

#### Services
- `services/publishService.py`: Handles message publishing operations
  - `publish_to_topic(message, topic_name)`: Publishes message to specific topic
  - `publish_to_all(message)`: Uses Singleton publisher to broadcast message to all topics

- `services/subscribeService.py`: Manages subscription operations and message retrieval
  - `subscribe(subscriber, topic_name)`: Subscribes user to topic
  - `unsubscribe(subscriber, topic_name)`: Removes subscription
  - `read_all_message(subscriber, topic_name)`: Retrieves all messages from topic
  - `read_last_message(subscriber, topic_name)`: Gets most recent message from topic

#### Repository
- `repository/topicsRepository.py`: Manages topic storage and operations
  - `create_topic(topic_name)`: Creates new topic
  - `get_topic(topic_name)`: Retrieves specific topic
  - `get_all_topics()`: Returns all available topics
  - `delete_topic(topic_name)`: Removes topic

### Main Module
- `pubsub.py`: Entry point demonstrating the system's functionality
  - Creates test topics and subscribers
  - Demonstrates subscription management
  - Shows message publishing and retrieval

## Singleton Publisher Pattern

The system implements a Singleton pattern for the Publisher class, ensuring:
- Only one publisher instance exists throughout the application
- Centralized message distribution
- Consistent message broadcasting to all topics
- Thread-safe publishing operations

## How It Works

1. **Topic Management**
   - Topics are created through TopicRepository
   - Each topic maintains its own message queue
   - Multiple subscribers can subscribe to the same topic

2. **Publishing**
   - Single publisher instance handles all publishing operations
   - Publishers can send messages to specific topics
   - Global broadcast capability to all topics
   - Messages are stored in topic-specific queues

3. **Subscribing**
   - Subscribers can subscribe to multiple topics
   - The SubscribeService manages subscriptions
   - Subscribers can:
     - Read all messages from a topic
     - Read only the last message from a topic
