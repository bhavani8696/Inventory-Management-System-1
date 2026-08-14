from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "inventory-management-1-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventory.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static", "uploads")
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255))

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def is_admin():
    if not current_user.is_authenticated:
        return False
    first = User.query.order_by(User.id.asc()).first()
    return bool(first and first.id == current_user.id)

PRODUCTS = [
("Wireless Bluetooth Earbuds","Electronics",899,25,"earbuds.svg"),
("Smart Watch Series 9","Electronics",1499,18,"watch.svg"),
("Bluetooth Speaker","Electronics",1299,20,"speaker.svg"),
("Fast Charging Power Bank","Electronics",1599,15,"powerbank.svg"),
("USB Type-C Charger","Electronics",499,40,"charger.svg"),
("Wireless Mouse","Electronics",399,35,"mouse.svg"),
("Gaming Keyboard","Electronics",1899,12,"keyboard.svg"),
("Gaming Headphones","Electronics",1099,22,"headphones.svg"),
("Mini Ring Light","Electronics",699,30,"ringlight.svg"),
("Smart LED Bulb","Electronics",299,50,"bulb.svg"),
("Cotton T-Shirt","Fashion",399,35,"tshirt.svg"),
("Women's Casual Kurti","Fashion",699,28,"kurti.svg"),
("Men's Slim Fit Shirt","Fashion",799,24,"shirt.svg"),
("Floral Dress","Fashion",899,20,"dress.svg"),
("Men's Casual Jeans","Fashion",1099,18,"jeans.svg"),
("Palazzo Pants","Fashion",549,32,"pants.svg"),
("Printed Saree","Fashion",999,16,"saree.svg"),
("Casual Hoodie","Fashion",899,20,"hoodie.svg"),
("Denim Jacket","Fashion",1199,14,"jacket.svg"),
("Sports Cap","Fashion",249,45,"cap.svg"),
("Matte Lipstick Set","Beauty",499,30,"lipstick.svg"),
("Vitamin C Face Serum","Beauty",599,25,"serum.svg"),
("Aloe Vera Face Gel","Beauty",299,40,"gel.svg"),
("Makeup Brush Set","Beauty",449,27,"brush.svg"),
("Waterproof Eyeliner","Beauty",199,45,"eyeliner.svg"),
("Face Wash Combo","Beauty",349,38,"facewash.svg"),
("Hair Care Gift Set","Beauty",799,18,"haircare.svg"),
("Body Lotion","Beauty",299,33,"lotion.svg"),
("Perfume For Women","Beauty",699,21,"perfume.svg"),
("Perfume For Men","Beauty",749,19,"perfume-men.svg"),
("Non Stick Frying Pan","Home",799,22,"pan.svg"),
("Steel Water Bottle","Home",499,35,"bottle.svg"),
("Ceramic Coffee Mug","Home",249,50,"mug.svg"),
("Decorative Table Lamp","Home",899,17,"lamp.svg"),
("Cushion Cover Set","Home",399,26,"cushion.svg"),
("Cotton Bedsheet","Home",999,15,"bedsheet.svg"),
("Kitchen Container Set","Home",699,23,"containers.svg"),
("Wall Photo Frame Set","Home",449,20,"frames.svg"),
("Artificial Indoor Plant","Home",599,18,"plant.svg"),
("Cleaning Cloth Set","Home",249,40,"cloth.svg"),
("Premium Cashew 500g","Grocery",549,30,"cashew.svg"),
("Organic Almonds 500g","Grocery",499,26,"almonds.svg"),
("Green Tea Pack","Grocery",299,35,"tea.svg"),
("Instant Coffee 200g","Grocery",349,31,"coffee.svg"),
("Mixed Dry Fruits 500g","Grocery",699,20,"dryfruits.svg"),
("Honey 500g","Grocery",399,25,"honey.svg"),
("Dark Chocolate Box","Grocery",299,42,"chocolate.svg"),
("Breakfast Oats 1kg","Grocery",249,36,"oats.svg"),
("Masala Combo Pack","Grocery",349,29,"masala.svg"),
("Basmati Rice 5kg","Grocery",699,18,"rice.svg"),
]

def seed():
    if Product.query.count() > 0:
        return
    for name, cat, price, qty, image in PRODUCTS:
        db.session.add(Product(product_name=name, category=cat, price=price, quantity=qty, image=image))
    db.session.commit()

with app.app_context():
    db.create_all()
    seed()

@app.context_processor
def globals():
    return {"admin_user": is_admin()}

@app.route("/")
@login_required
def dashboard():
    total = Product.query.count()
    stock = sum(p.quantity for p in Product.query.all())
    categories = db.session.query(Product.category).distinct().count()
    low = Product.query.filter(Product.quantity <= 5).count()
    return render_template("dashboard.html", total=total, stock=stock, categories=categories, low=low)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        if User.query.filter_by(email=email).first():
            flash("Email already registered.", "error")
            return redirect(url_for("register"))
        db.session.add(User(name=name, email=email, password=generate_password_hash(password)))
        db.session.commit()
        flash("Registration successful. Please login.", "success")
        return redirect(url_for("login"))
    return render_template("login.html", register=True)

@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        email = request.form["email"].strip().lower()
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("dashboard"))
        flash("Invalid email or password.", "error")
    return render_template("login.html", register=False)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/products")
@login_required
def products():
    search = request.args.get("search","").strip()
    category = request.args.get("category","").strip()
    q = Product.query
    if search:
        q = q.filter(Product.product_name.ilike(f"%{search}%"))
    if category:
        q = q.filter_by(category=category)
    items = q.order_by(Product.id.desc()).all()
    cats = [x[0] for x in db.session.query(Product.category).distinct().order_by(Product.category)]
    return render_template("products.html", products=items, categories=cats, search=search, selected=category)

@app.route("/product/<int:id>")
@login_required
def details(id):
    return render_template("details.html", product=Product.query.get_or_404(id))

@app.route("/add-product", methods=["GET","POST"])
@login_required
def add_product():
    if not is_admin():
        flash("Only admin can add products.", "error")
        return redirect(url_for("products"))
    if request.method == "POST":
        image = request.files.get("image")
        filename = secure_filename(image.filename) if image and image.filename else "default.svg"
        if image and image.filename:
            image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        p = Product(product_name=request.form["product_name"], category=request.form["category"],
                    price=float(request.form["price"]), quantity=int(request.form["quantity"]), image=filename)
        db.session.add(p); db.session.commit()
        flash("Product added successfully.", "success")
        return redirect(url_for("products"))
    return render_template("product_form.html", product=None)

@app.route("/edit/<int:id>", methods=["GET","POST"])
@login_required
def edit(id):
    if not is_admin():
        flash("Only admin can edit products.", "error")
        return redirect(url_for("products"))
    p = Product.query.get_or_404(id)
    if request.method == "POST":
        p.product_name=request.form["product_name"]; p.category=request.form["category"]
        p.price=float(request.form["price"]); p.quantity=int(request.form["quantity"])
        image=request.files.get("image")
        if image and image.filename:
            filename=secure_filename(image.filename); image.save(os.path.join(app.config["UPLOAD_FOLDER"],filename)); p.image=filename
        db.session.commit(); flash("Product updated successfully.","success")
        return redirect(url_for("products"))
    return render_template("product_form.html", product=p)

@app.route("/delete/<int:id>", methods=["POST"])
@login_required
def delete(id):
    if not is_admin():
        flash("Only admin can delete products.", "error")
        return redirect(url_for("products"))
    p=Product.query.get_or_404(id); db.session.delete(p); db.session.commit()
    flash("Product deleted successfully.","success")
    return redirect(url_for("products"))

@app.route("/wishlist")
@login_required
def wishlist():
    return render_template("wishlist.html")

@app.route("/cart")
@login_required
def cart():
    return render_template("cart.html")

@app.route("/api/product/<int:id>")
@login_required
def product_api(id):
    p=Product.query.get_or_404(id)
    return jsonify(id=p.id,name=p.product_name,category=p.category,price=p.price,quantity=p.quantity,
                   image=url_for("static",filename="uploads/"+p.image) if p.image else "")

if __name__ == "__main__":
    app.run(debug=True)
