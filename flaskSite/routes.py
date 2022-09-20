from flask import render_template, url_for, flash, redirect, request, session
from flaskSite import app, mongo, get_all_items
from flaskSite import clc_processor, clc_cabinet, clc_cooler, clc_graphicscard, clc_harddrive, clc_memory, clc_monitor, clc_motherboard, clc_ssd, cld_powersupply, clc_users, clc_orders
from flaskSite.forms import *
from bson.objectid import ObjectId
import datetime


@app.before_request
def make_session_permanent():
    session.permanent = True


@app.route("/")
def homepage():
    items = get_all_items()
    return render_template("index.html", titleVal="DG-Computer", userid=session.get("USERID"), username=session.get("USERNAME"), items=items)


@app.route("/dashboard")
def dashboard():
    if session.get("userid") == 1:
        items = get_all_items()
        users = list(clc_users.find())
        return render_template("dashboard.html", items=items, users=users)
    else:
        return "<h1>404</h1>"


@app.route("/dashboard/addproduct", methods=['GET', 'POST'])
def addProduct():
    form = ProductUploadForm()
    
    if request.method == "POST":
        product = {}
        
        product["name"] = form.productname.data.strip()
        product["price"] = form.productcost.data
        product["quantity"] = form.productquantity.data
        
        producttype = form.producttype.data
        productimage = form.productimage.data
        
        insertion_query = f"clc_{producttype.lower()}.insert_one({product})"
        #print(insertion_query)
        obj_id = eval(insertion_query)
        #print(obj_id.inserted_id)
        productimagesavepath = f"./flaskSite/static/{producttype.lower()}/"
        productimage.save(f"{productimagesavepath}{obj_id.inserted_id}.jpg")
        
        flash(f"{producttype.capitalize()} added successfully!", 'success')
        return redirect("/dashboard/addproduct")
    
    return render_template("addProduct.html", form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        user = {}
        
        user["username"] = form.username.data.lower()
        user["email"] = form.email.data.lower()
        user["password"] = form.password.data
        
        if user["password"] != form.confirm_password.data:
            flash("Passwords doesn't matched", 'warning')
            return redirect("/register")
        
        user_with_same_email_exists = list(clc_users.find({"email": user["email"]}))
        if user_with_same_email_exists:
            flash('Email already exists. You can log in.', 'warning')
        else:
            user_with_same_username_exists = list(clc_users.find({"username": user["username"]}))
            if user_with_same_username_exists:
                flash('Username already exists. Please choose a different one!', 'warning')
            elif not 2 <= len(user["username"]) <= 20:
                flash('Choose a username within 2 to 20 characters!', 'warning')
            else:
                clc_users.insert_one(user)
                flash('You are successfully registered!', 'success')
        
        return redirect("/register")
    
    return render_template("register.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if request.method == "POST":
        user = {}
        
        user["email"] = form.email.data.lower()
        user["password"] = form.password.data
        rememberMe = form.rememberMe.data
        

        user = clc_users.find_one({"email": user["email"], "password": user["password"]})
        if user:
            session["USERNAME"] = user["username"]
            session["USERID"] = 1 if user["email"] == "admin@gmail.com" else str(user["_id"])

            if not rememberMe:
                app.permanent_session_lifetime = datetime.timedelta(days=31)
            else:
                make_session_permanent()
            
            return homepage()
        
        else:
            flash('Invalid Credentials!', 'warning')
            return redirect("/login")
        
        
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session["USERNAME"] = ""
    session["USERID"] = 0
    return homepage()


@app.route("/processor/<pid>")
def showOrSellProcessor(pid):
    product = clc_processor.find_one({"_id": ObjectId(pid)})
    imagepath = f"processor/{pid}.jpg"
    return render_template("product.html", titleVal="DG-Computer", userid=session.get("USERID"), username=session.get("USERNAME"), product=product, imagepath=imagepath)


@app.route("/products/<category>")
def showProduct(product):
    return "<h1>Asche Asche</h1>"