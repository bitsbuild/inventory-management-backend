# 📦 InventoryManagementREST-drf-backend

A Django REST Framework backend for managing inventory items with complete CRUD functionality. Includes Swagger documentation for easy API exploration and testing.

---

## 📚 Overview

This project provides a simple REST API to create, retrieve, update, and delete inventory items. Each item includes details like name, description, category, quantity, and price.

This backend serves as a practice ground to reinforce concepts such as:

- APIView class-based views
- Serializer usage (non-model)
- UUID-based primary keys
- Manual URL routing
- Swagger UI integration with `drf-yasg`

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.9+
- pip
- Virtual environment (optional but recommended)

### 📦 Installation

```bash
# Clone the repository
git clone https://github.com/bitsbuild/InventoryManagementREST-drf-backend-basics-reinforcement.git
cd inventory

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run the development server
python manage.py runserver
````

---

## 🛠️ API Endpoints

### 🧾 POST & GET (All Items)

* **POST `/inventory/restapis/pg/`**
  Create a new item in the inventory.
  Required JSON fields:

  ```json
  {
    "item_name": "string",
    "item_description": "string",
    "item_category": "one of the supported categories",
    "item_quantity": int,
    "item_price": int
  }
  ```

* **GET `/inventory/restapis/pg/`**
  Fetch all items in the inventory. Returns a list of all items with their details.

---

### 🔍 GET, PUT & DELETE (Single Item by UUID)

* **GET `/inventory/restapis/gud/<uuid:id>`**
  Fetch details of a specific item by UUID.

* **PUT `/inventory/restapis/gud/<uuid:id>`**
  Update the details of a specific item by UUID. Requires full item data in the request body.

* **DELETE `/inventory/restapis/gud/<uuid:id>`**
  Delete a specific item by UUID. Returns a success or failure message.

---

## 📑 Categories Supported

* clothing
* electronics
* home\_appliances
* furniture
* books
* toys
* beauty
* sports
* groceries
* footwear
* stationery
* automotive
* jewelry
* pet\_supplies
* music
* gaming
* mobile\_accessories
* luggage
* health
* baby\_products

---

## 🧠 Learn More

This project is ideal if you're looking to strengthen your knowledge in:

* Django REST Framework fundamentals
* Class-based API views (`APIView`)
* Manual serializers
* Swagger / OpenAPI integration

---

## 🪪 License

This project is licensed under the MIT License.

---

**Build strong backends — because solid foundations power great software. 💡**
