# 🍝 🦐 Restaurant Orders 🍛 🥘

Welcome to the **Restaurant Orders** project repository, a menu-building tool for the **Restaurant Orders** restaurant! This project was developed as part of a course, focused on practicing essential programming and software development skills.

---

## 📝 About the Project

**Restaurant Orders** is an application that helps the restaurant generate personalized menus, taking into account possible dietary restrictions and the availability of ingredients in stock. Currently, the restaurant manages recipes and inventory through CSV files, which makes the process inefficient. This project aims to optimize this management and offer a practical and efficient solution.

In this project you will find:

- Classes to map dishes, recipes, and ingredients.
- Features to generate personalized menus.
- A system to manage ingredient inventory.
- Automated tests to ensure code quality.

---

## 🚵 Skills Practiced

During the development of this project, the following skills were practiced:

- **Use of Hashmaps**: `Dict` and `Set` data structures in Python.
- **Software Testing**: Implementation and execution of tests to ensure the code works correctly.
- **Object Orientation**: Design and implementation of classes to organize the project's logic.

---

## 📂 Project Structure

The project is organized as follows:

```plaintext
📁 data/
   ├── inventory_base_data.csv  # Base inventory data
   └── menu_base_data.csv       # Base menu data

📁 src/
   ├── models/                  # Core models
   │   ├── dish.py              # Class representing dishes
   │   ├── ingredient.py        # Class representing ingredients
   │   └── __init__.py
   ├── services/                # Core services
   │   ├── inventory_control.py # Inventory control
   │   ├── menu_builder.py      # Menu building
   │   ├── menu_data.py         # Menu data handling
   │   └── __init__.py
   ├── app.py                   # Application entry point
   └── __init__.py

📁 tests/                       # Automated tests
   ├── dish/
   │   ├── test_dish.py         # Tests for the Dish class
   │   └── __init__.py
   ├── ingredient/
   │   ├── test_ingredient.py   # Tests for the Ingredient class
   │   └── __init__.py
   └── __init__.py
```

---

## 🛠️ How to Run the Project

1. Clone this repository:

    ```bash
    git clone https://github.com/vicentevendramin/restaurant-orders.git
    cd restaurant-orders
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt # Production
    pip install -r dev-requirements.txt # Development
    ```

4. Run the tests to verify everything works:

    ```bash
    pytest # Development
    ```
