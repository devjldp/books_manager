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
