# Inventory Management System

A full-stack **Inventory Management System** developed using **Python Flask, Flask-SQLAlchemy, Flask-Login, HTML, CSS and JavaScript**.

This application helps manage products, stock quantities, categories, product images, user authentication, wishlist and cart features through a simple and user-friendly web interface.

---

## 🚀 Live Demo

👉 https://inventory-management-system-1-3.onrender.com

## 💻 GitHub Repository

👉 https://github.com/bhavani8696/Inventory-Management-System-1

> **Note:** The application is deployed on Render's free service. If the application has been inactive for some time, it may take a few seconds to wake up.

---

# 📌 Project Overview

The **Inventory Management System** is a web-based application designed to simplify product and inventory management.

The application provides a centralized platform where users can access products and administrators can manage inventory.

### Main Features

* User Registration
* User Login and Logout
* Admin Authentication
* Dashboard
* Product Management
* Add Product
* Edit Product
* Delete Product
* Product Search
* Category Filtering
* Product Details
* Wishlist
* Shopping Cart
* Product Images
* Stock Management
* Low Stock Tracking
* Product Export
* SQLite Database
* Responsive Web Interface

The main purpose of this project is to provide an organized platform for managing products and inventory efficiently.

---

# 🎯 Project Objectives

The main objectives of this project are:

* To develop a web-based inventory management system.
* To implement secure user registration and login.
* To manage products using a database.
* To provide an inventory dashboard.
* To display products with images and details.
* To implement product search.
* To implement category-based filtering.
* To provide product details.
* To implement wishlist functionality.
* To implement shopping cart functionality.
* To provide admin-based product management.
* To implement CRUD operations.
* To track stock and low-stock products.
* To deploy the application online.

---

# 🛠️ Technologies Used

## Frontend

* HTML5
* CSS3
* JavaScript
* Jinja2 Templates

## Backend

* Python
* Flask
* Flask-Login
* Flask-SQLAlchemy
* Werkzeug

## Database

* SQLite

## Data Processing

* Pandas

## Deployment

* Render
* Gunicorn

## Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
Inventory-Management-System-1/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── README.md
├── README_FINAL.md
├── products.csv
├── render.yaml
│
├── instance/
│   └── inventory.db
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── app.js
│   │
│   └── uploads/
│       └── product images
│
└── templates/
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── products.html
    ├── product_details.html
    ├── add_product.html
    ├── edit_product.html
    ├── wishlist.html
    └── cart.html
```

---

# 📄 File Explanation

## 1. app.py

`app.py` is the main Flask application file.

It contains the main application logic, routes and functionality required to connect the frontend with the database.

The file handles:

* User registration
* User login
* User logout
* Dashboard
* Products
* Product search
* Category filtering
* Product details
* Wishlist
* Cart
* Add product
* Edit product
* Delete product
* Admin authorization
* Inventory management
* Product export

It acts as the main controller of the application.

---

## 2. models.py

`models.py` contains the database models used by the application.

The application mainly works with user and product-related database information.

### User

The User model stores information required for user authentication.

### Product

The Product model stores product information such as:

* Product name
* Category
* Price
* Quantity
* Product image
* Stock information

Flask-SQLAlchemy is used to communicate with the SQLite database.

---

## 3. config.py

`config.py` contains configuration information required by the Flask application.

Keeping configuration separately makes the project easier to maintain and organize.

---

## 4. requirements.txt

`requirements.txt` contains the Python packages required to run the application.

The project uses dependencies such as:

* Flask
* Flask-SQLAlchemy
* Flask-Login
* Werkzeug
* Gunicorn

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## 5. products.csv

`products.csv` contains product-related inventory data.

It can be used as an input source for product information.

---

## 6. render.yaml

`render.yaml` contains deployment-related configuration for deploying the application on Render.

It helps define the service configuration required for deployment.

---

# 🎨 Templates

The `templates` folder contains the Jinja2 HTML pages used by the application.

## login.html

Provides the login interface for existing users.

## register.html

Allows new users to create an account.

## dashboard.html

Displays the main inventory dashboard and important inventory information.

## products.html

Displays the available products with their images and details.

## product_details.html

Displays detailed information about a selected product.

## add_product.html

Provides a form for authorized administrators to add a new product.

## edit_product.html

Allows administrators to update existing product information.

## wishlist.html

Displays products saved by the user in the wishlist.

## cart.html

Displays products added to the shopping cart.

---

# 🎨 Static Files

The `static` folder contains the frontend resources.

It includes:

* CSS
* JavaScript
* Product images

### CSS

The CSS file is responsible for the design, layout and styling of the application.

### JavaScript

JavaScript is used for frontend interactions and user interface behavior.

### Uploads

The uploads folder contains product images displayed in the application.

---

# 🔐 User Registration and Login

The application provides a user authentication system.

New users can register using the registration page.

Existing users can log in using their credentials.

**Flask-Login** is used for session management and authentication.

After successful login, the user is redirected to the dashboard.

---

# 📊 Dashboard

The dashboard provides an overview of the inventory.

It helps administrators understand the current inventory status quickly.

The dashboard includes information related to:

* Total Products
* Categories
* Stock Quantity
* Low Stock Products

This reduces the need to manually check every product.

---

# 📦 Products

The Products page displays all available products.

Products are displayed with important information such as:

* Product Image
* Product Name
* Category
* Price
* Quantity

The structured product layout makes it easier to browse the inventory.

---

# 🔎 Product Search

The application provides a search functionality.

Users can search for products using the product name or relevant search text.

This makes it easier to find a particular product without manually checking the complete product list.

---

# 🏷️ Category Filtering

Products can be filtered according to their category.

This helps users quickly find products belonging to a specific category.

Search and filtering improve the overall product browsing experience.

---

# 🔍 Product Details

Users can select a product to view its detailed information.

The product details page provides information such as:

* Product Name
* Category
* Price
* Available Quantity
* Product Image

---

# ❤️ Wishlist

The application provides a Wishlist feature.

Users can save products that they are interested in for later viewing.

The Wishlist page displays the products saved by the user.

---

# 🛒 Shopping Cart

The application also provides a Shopping Cart feature.

Users can add selected products to their cart and view the products they have chosen.

This provides a convenient way to manage selected products.

---

# 👨‍💼 Admin Product Management

The application provides additional product management features for authorized administrators.

The admin can:

* Add products
* View products
* Edit products
* Delete products

This allows the administrator to maintain updated inventory information.

---

# ➕ Add Product

The admin can add a new product using the Add Product page.

Product information can include:

* Product Name
* Category
* Price
* Quantity
* Product Image

After submitting the form, the product information is stored in the database.

---

# ✏️ Edit Product

The Edit Product feature allows administrators to update existing products.

The administrator can update product information such as:

* Name
* Category
* Price
* Quantity
* Image

This helps keep inventory information accurate.

---

# 🗑️ Delete Product

The admin can delete products that are no longer required.

This helps maintain clean and updated inventory records.

---

# 🔄 CRUD Operations

The project demonstrates basic CRUD operations.

### Create

Adding a new product to the inventory.

### Read

Displaying products, dashboard information and product details.

### Update

Editing existing product information.

### Delete

Removing products from the inventory.

These operations provide the basic functionality required for product management.

---

# 📦 Stock Management

The system stores product quantities and provides inventory-related information.

The dashboard also helps identify products with low stock.

This allows administrators to monitor inventory more effectively.

---

# 🔐 Authentication and Authorization

The project implements authentication using Flask-Login.

Users need to authenticate before accessing protected features.

Admin authorization is also implemented.

Administrators have access to product management operations such as:

* Add
* Edit
* Delete

This separates normal user functionality from administrative functionality.

---

# 🗄️ Database

The application uses **SQLite** as its database.

**Flask-SQLAlchemy** is used as the ORM layer.

The database is used to store application information such as:

* User information
* Product information
* Inventory information

This allows the application to dynamically store and retrieve data.

---

# 🔗 Application Workflow

```text
User
  ↓
Registration / Login
  ↓
Dashboard
  ↓
Products
  ↓
Search / Category Filter
  ↓
Product Details
  ↓
Wishlist / Cart

Admin
  ↓
Dashboard
  ↓
Product Management
  ↓
Add Product
  ↓
Edit Product
  ↓
Delete Product
```

---

# ▶️ How to Run Locally

## Step 1: Clone the Repository

```bash
git clone https://github.com/bhavani8696/Inventory-Management-System-1.git
```

## Step 2: Open the Project

```bash
cd Inventory-Management-System-1
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
python app.py
```

## Step 5: Open in Browser

```text
http://127.0.0.1:5000
```

---

# ☁️ Deployment

The application is deployed using **Render**.

Gunicorn is used as the production WSGI server.

The source code is maintained using GitHub.

### GitHub Repository

https://github.com/bhavani8696/Inventory-Management-System-1

### Live Application

https://inventory-management-system-1-3.onrender.com

---

# 🧪 Project Demonstration Flow

The project can be demonstrated in the following order:

1. Open GitHub Repository.
2. Show README.
3. Explain project overview.
4. Show project structure.
5. Open `app.py`.
6. Explain the main application logic.
7. Show `models.py`.
8. Explain the database models.
9. Show `templates` folder.
10. Show `static` folder.
11. Show `requirements.txt`.
12. Open the Live Demo.
13. Demonstrate Registration/Login.
14. Show Dashboard.
15. Show Products.
16. Demonstrate Search.
17. Demonstrate Category Filter.
18. Open Product Details.
19. Show Wishlist.
20. Show Cart.
21. Show Admin Product Management.
22. Demonstrate Add Product.
23. Demonstrate Edit Product.
24. Demonstrate Delete Product.
25. Explain CRUD operations.
26. Conclude the project.

---

# 🌟 Key Benefits

The Inventory Management System provides:

* Simple inventory management
* Centralized product information
* User authentication
* Admin authorization
* Product search
* Category filtering
* Product details
* Wishlist functionality
* Cart functionality
* CRUD operations
* Stock tracking
* Low-stock tracking
* Product image management
* Online deployment

---

# 🔮 Future Enhancements

The project can be further improved by adding:

* MySQL or PostgreSQL database
* Complete order management
* Payment gateway integration
* Email notifications
* Automated low-stock alerts
* Sales analytics
* Inventory reports
* Advanced admin dashboard
* Automated testing
* CI/CD pipeline
* Cloud database integration
* Application monitoring and logging

---

# 🎓 Learning Outcomes

Through this project, I gained practical experience in:

* Python Flask development
* Backend development
* Database integration
* Flask-SQLAlchemy
* User authentication
* Admin authorization
* CRUD operations
* HTML and CSS
* JavaScript
* Jinja2 templates
* Git and GitHub
* Application deployment
* Gunicorn
* Render deployment

---

# 🏁 Conclusion

The **Inventory Management System** is a full-stack web application developed to simplify product and inventory management.

The project demonstrates user authentication, database management, inventory tracking, product search and filtering, product details, wishlist, shopping cart and admin-based product management.

The application follows a structured architecture where the Flask backend handles application logic, SQLite stores the data, and HTML, CSS, JavaScript and Jinja2 provide the user interface.

The project was developed, maintained using GitHub and deployed using Render.

Overall, this project provided practical experience in developing a complete web application from backend and database integration to frontend development, authentication, CRUD operations and deployment.

---

## 🔗 Project Links

### GitHub Repository

https://github.com/bhavani8696/Inventory-Management-System-1

### Live Demo

https://inventory-management-system-1-3.onrender.com

### Video Demo

https://drive.google.com/file/d/1W70tpi5wqXZ2r2i6R3yPjZaASy2Hzk0y/view?usp=sharing

---

**Thank you for visiting my Inventory Management System project! 🚀**
