# Import the os module to work with operating system functionalities
import os
# Import necessary classes and functions from Flask and Flask-PyMongo
from flask import (Flask, flash, render_template,
                  redirect, request, session, url_for)
# Import PyMongo to interact with MongoDB from Flask
from flask_pymongo import PyMongo

from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash



# Check if the "env.py" file exists and, if so, import its environment variables
if os.path.exists("env.py"):
    import env

# Create an instance of the Flask application
app = Flask(__name__)

# Configuration of the MongoDB database and the secret key for the session
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Routes
@app.route('/')
def index():
    return render_template("index.html")

# Register a new user 
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # Check if the email already exists in the database
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
    
        if existing_user or existing_email:
            # If the user already exists, display an error message and redirect to the registration page
            flash("Username /email already exists")
            return redirect(url_for("register"))
    
        # Register the new user in the database
        register = {
            "name": request.form.get("name").lower(),
            "email": request.form.get("email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        
        # insert the new user in my db
        mongo.db.users.insert_one(register)
        
        # Start a session for the new user
        session["user"] = request.form.get("username").lower()
        flash("Registration successful!")
    
    return render_template("register.html")

# Sign In
@app.route('/signin', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
    # Check if the user exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            # If the user exists, verify the password
            if check_password_hash(existing_user["password"], request.form.get("password")):
                if existing_user["username"] != 'admin':
                    # If the password is correct, log in and redirect to the profile
                    session["user"] = request.form.get("username").lower()
                    flash(f"Welcome, {request.form.get('username')}")
                    return redirect(url_for("profile", username=session["user"]))
                else:
                    session["user"] = request.form.get("username").lower()
                    flash(f"Manager: {request.form.get('username')}") 
                    return redirect(url_for("admin", username=session["user"]))  
            else:
                # If the password is incorrect, display an error message and redirect to the login
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
            # If the user does not exist, display an error message and redirect to the login
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
    
    return render_template("login.html")

# view for users
@app.route("/profile/<username>")
def profile(username):
    # Get the username from the current session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Check if there is an active user session
    if session["user"]:
        # Render the "profile.html" template and pass the username as an argument
        return render_template("profile.html", username=username)
    # If there is no active session, redirect to the login
    return redirect(url_for("login"))


# view for administrator
@app.route("/admin/<username>")
def admin(username):
    # Get the username from the current session
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # Check if there is an active user session
    if session["user"]:
        # Render the "profile.html" template and pass the username as an argument
        return render_template("admin.html", username=username)
    # If there is no active session, redirect to the login
    return redirect(url_for("login"))

# Define log out
@app.route("/logout")
def logout():
    # Display a farewell message and clear the user session
    flash("You have been logged out")
    session.pop("user")
    # Redirect to the login page
    return redirect(url_for('index'))


@app.route('/books')
def getBooks():
    books = mongo.db.books.find()
    return render_template("books.html", books=books)





# If this file is executed as the main script
if __name__ == "__main__":
    # Run the Flask application with the configuration from environment variables
    app.run(
        host=os.environ.get("IP"),  # Get the IP from environment variables
        port=int(os.environ.get("PORT")),  # Get the port from environment variables
        # Enable debug mode --> For the project, it should be set to False
        debug=True 
    )
