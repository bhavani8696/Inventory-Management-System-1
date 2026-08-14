# Inventory Management System

A full-stack **Inventory Management System** built using **Python, Flask, SQLite, HTML, CSS, JavaScript, Flask-SQLAlchemy and Flask-Login**.

The application provides a simple and user-friendly platform for managing products, inventory, categories, wishlist and shopping cart operations.

## 🚀 Live Demo

Live Application:

https://inventory-management-system-1-1.onrender.com

## 📂 GitHub Repository

https://github.com/bhavani8696/Inventory-Management-System-1

---

# 📌 Project Overview

The Inventory Management System is a web-based application designed to manage products and inventory efficiently.

The application provides separate functionality for administrators and customers.

Administrators can:

- Login securely
- View the dashboard
- View all products
- Search products
- Filter products by category
- Add new products
- Edit products
- Delete products
- Manage product quantity
- View inventory statistics
- Export product data

Customers can:

- Register an account
- Login securely
- View the dashboard
- Browse products
- Search products
- Filter products
- View product details
- Add products to wishlist
- Add products to cart
- Remove products from wishlist
- Remove products from cart
- View saved products

---

# ✨ Features

## 1. User Registration

New users can create an account by providing:

- Name
- Email
- Password

Passwords are securely stored using password hashing.

---

## 2. User Login

Registered users can login using their email and password.

The application uses **Flask-Login** for user authentication and session management.

---

## 3. Dashboard

The dashboard provides an overview of the inventory.

It displays:

- Total Products
- Total Categories
- Total Stock
- Low Stock Products

This helps the administrator quickly understand the current inventory status.

---

## 4. Product Management

The administrator can manage products through the product management section.

Each product contains:

- Product Name
- Category
- Price
- Quantity
- Product Image

---

## 5. Add Products

Administrators can add new products by entering product information and uploading an image.

Product information is stored in the SQLite database.

---

## 6. Edit Products

The administrator can update existing product information.

The following information can be updated:

- Product Name
- Category
- Price
- Quantity
- Product Image

---

## 7. Delete Products

Administrators can delete products from the inventory.

When a product is deleted, its database record is removed and the associated uploaded image can also be removed.

---

## 8. Search Products

Users can search products using the product search option.

The search functionality helps users quickly find products based on their names.

---

## 9. Category Filter

Products can be filtered according to their category.

Example categories include:

- Electronics
- Fashion
- Beauty
- Home
- Grocery

---

## 10. Product Details

Users can open individual products and view detailed information such as:

- Product name
- Category
- Price
- Available quantity
- Product image

---

## 11. Wishlist

Users can add products to their wishlist.

The wishlist allows users to save products they may want to view or purchase later.

Wishlist functionality is handled on the frontend using browser local storage.

---

## 12. Shopping Cart

Users can add products to their cart.

The cart displays:

- Selected products
- Product price
- Available quantity
- Total cart value

Users can also remove products from the cart.

---

## 13. Responsive Product Layout

Products are displayed in a clean card-based layout.

The interface is designed to display multiple products in rows, making it easier for users to browse the marketplace.

---

## 14. Product Images

Products can contain uploaded images.

Images are stored inside the:

`static/uploads`

directory.

---

## 15. Admin Access

The first registered account is treated as the personal/admin account.

Only the administrator can access:

- Add Product
- Edit Product
- Delete Product
- Export Products

Customers can browse and use shopping features without seeing the admin management options.

---

# 🛠️ Technologies Used

## Backend

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug

## Frontend

- HTML5
- CSS3
- JavaScript
- Font Awesome

## Database

- SQLite

## Data Processing

- Pandas

## Deployment

- Render

## Version Control

- Git
- GitHub

---

# 🏗️ Project Structure

```text
Inventory-Management-System-1/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── README.md
├── products.csv
│
├── instance/
│   └── inventory.db
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── uploads/
│
└── templates/
    ├── login.html
    ├── register.html
    ├── dashboard.html
    ├── products.html
    ├── product_details.html
    ├── wishlist.html
    ├── cart.html
    ├── add_product.html
    └── edit_product.html
