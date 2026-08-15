# Inventory Management System

A full-stack **Inventory Management System** developed using **Python Flask, Flask-SQLAlchemy, Flask-Login, HTML, CSS and JavaScript**.

This application helps manage products, stock quantities, categories, product images, user authentication, wishlist and cart features through a simple and user-friendly web interface.

## 🚀 Live Demo

👉 https://inventory-management-system-1-3.onrender.com

## 🚀 Vedio demo link
👉 https://drive.google.com/file/d/1W70tpi5wqXZ2r2i6R3yPjZaASy2Hzk0y/view?usp=sharing

> Note: The Render free service may sleep when inactive. If the application takes a few seconds to open, please wait for the service to wake up.

---

## 📌 Project Overview

The Inventory Management System is designed to simplify inventory management for an administrator.

The application provides:

- User Registration
- User Login and Logout
- Admin Authentication
- Dashboard
- Product Management
- Add Product
- Edit Product
- Delete Product
- Product Search
- Category Filtering
- Product Details
- Wishlist
- Shopping Cart
- Product Images
- Stock Management
- Low Stock Tracking
- Product Export
- SQLite Database
- Responsive Web Interface

The main purpose of this project is to provide an organized platform for managing products and inventory efficiently.

---

## 🛠️ Technologies Used

### Frontend

- HTML5
- CSS3
- JavaScript
- Jinja2 Templates

### Backend

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- Werkzeug

### Database

- SQLite

### Data Processing

- Pandas

### Deployment

- Render
- Gunicorn

### Version Control

- Git
- GitHub

---

## 📂 Project Structure

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
