# E-Commerce NoSQL

E-commerce API built with FastAPI, DynamoDB and Redis.

## Tech Stack

### Backend
- **FastAPI** - Web framework
- **DynamoDB Local** - NoSQL database
- **Redis** - Cache layer
- **boto3** - AWS SDK for Python
- **Docker** - Local infrastructure

### Frontend
- **React + Vite** - Frontend framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling

## Prerequisites

- Python 3.x
- Docker Desktop
- Node.js
- Git

## Backend Setup

### 1. Clone the repository
git clone <repository-url>
cd E-CommerceNOSQL

### 2. Create virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
cp .env.example .env

### 5. Start Docker services
docker-compose up -d

### 6. Create the database table
python scripts/create_table.py

### 7. Load sample data (optional)
python scripts/seed_data.py

### 8. Run the API
cd src
uvicorn app.main:app --reload

API will be available at:
- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs - Swagger UI
- http://127.0.0.1:8000/redoc - ReDoc

## Frontend Setup

### 1. Install dependencies
cd src/frontend
npm install

### 2. Run the frontend
npm run dev

Frontend will be available at http://localhost:5173

## API Endpoints

### Users
- GET /users/{user_id} - Get user profile
- GET /users/{user_id}/orders - Get orders by user
- GET /users/{user_id}/payment-methods - Get payment methods by user
- GET /users/{user_id}/addresses - Get addresses by user
- POST /users - Create user

### Orders
- GET /orders/{order_id} - Get order detail
- GET /orders/{order_id}/items - Get items by order
- POST /orders - Create order