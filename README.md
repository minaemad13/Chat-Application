# Chat Application

Welcome to the Chat Application, a real-time messaging platform built with Django, Django Channels, and WebSockets.
This project aims to provide a scalable, secure, and user-friendly platform for group chats.

## Features

- **Real-time messaging:** Enjoy instant communication with minimal latency.
- **Group chats:** Create and manage group conversations.
- **Scalable architecture:** Designed to handle a growing number of users efficiently.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9.13
- Django
- Django Channels
- Docker

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/minaemad13/Chat-Application.git

2. Navigate to the project directory:
   ```bash
      cd Chat-Application

4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt

6. Install and Run Radies Container:
    ```bash
   docker run -p 6379:6379 redis:7
8. Run The Application:
    ```bash
   python manage.py runserver        
