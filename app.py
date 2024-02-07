# Import the os module to work with operating system functionalities
import os
# Import necessary classes and functions from Flask and Flask-PyMongo
from flask import (Flask, flash, render_template,
                  redirect, request, session, url_for)
# Import PyMongo to interact with MongoDB from Flask
from flask_pymongo import PyMongo
# pagination 
from flask_paginate import Pagination, get_page_parameter
from flask import Blueprint

mod = Blueprint('books', __name__)

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


# routes for admin 
# Add a new book
@app.route("/add_book.html", methods = ["GET", "POST"])
def add_book():
    if request.method == "POST":
        # Check if the book already exists in the database
        existing_book = mongo.db.books.find_one(
            {"title": request.form.get("title").lower()})

        if existing_book:
            # If the book already exists, display an error message and redirect to the add book page
            flash("This book already exists in the database")
            return redirect(url_for("add_book"))
    
        # Add the new book in the database
        book = {
            "title": request.form.get("title").lower(),
            "author": request.form.get("author").lower(),
            "year_published": int(request.form.get("year_published")),
            "genre": request.form.get("genre").lower(),
            "isbn":  request.form.get("isbn"),
            "publisher": request.form.get("publisher"),
            "language": request.form.get("language").lower(),
            "description": request.form.get("description")
        }
        
        # insert the new book in my db
        mongo.db.books.insert_one(book)
        # display a message 
        flash("Book Successfully Added!")
    
    return render_template("add_book.html")

@app.route('/books')
def get_books():
    search = False    
    # Number of books per page
    books_per_page = 10
    # Get the current page number from the URL query
    page = request.args.get(get_page_parameter(), type=int, default=1)
    # Calculate the start index for pagination
    start_index = (page - 1) * books_per_page
    # MongoDB query with limit and skip for pagination
    books = list(mongo.db.books.find().skip(start_index).limit(books_per_page))

    total = mongo.db.books.count_documents({})  # Total number of books in the collection
    pagination = Pagination(page=page, total=total, search=search, record_name='books', per_page=books_per_page)
    return render_template("books.html", books=books, pagination=pagination)


# Define the route "/edit_task/<task_id>" to edit an existing task
@app.route("/edit_book/<book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
    # Create a dictionary with the upddated book information
        updatedBook = {
            "title": request.form.get("title").lower(),
            "author": request.form.get("author").lower(),
            "year_published": int(request.form.get("year_published")),
            "genre": request.form.get("genre").lower(),
            "isbn":  request.form.get("isbn"),
            "publisher": request.form.get("publisher"),
            "language": request.form.get("language").lower(),
            "description": request.form.get("description")
        }
        # Update the task in the database using its ID
        mongo.db.books.update_one({"_id": ObjectId(book_id)}, {"$set": updatedBook})
        
        # Display a success message using flash
        flash("Book Successfully Updated!")
        return redirect(url_for("get_books"))

    # Get the book from the database to display it in the user interface
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})

    # Render the HTML template to edit the task with the obtained data
    return render_template("edit_book.html", book=book)

# Define the route to delete a task with its ID
@app.route("/delete_book/<book_id>")
def delete_book(book_id):
    # Delete the task from the database using its ID
    mongo.db.books.delete_one({"_id": ObjectId(book_id)})
    # Display a success message using flash
    flash("Book Successfully Deleted")
    # Redirect to the page that shows all tasks
    return redirect(url_for("get_books"))

# routes for users

@app.route('/books/<username>')
def get_user_books(username):
    books = mongo.db.books.find()
    return render_template("books_user.html", books=books)


@app.route('/view_book/<book_id>',  methods=["GET", "POST"])
def view_book(book_id):
    if request.method == "POST":
    # Create a dictionary with the upddated book information
        review = {
            "book": request.form.get("book").lower(),
            "user": session["user"],
            "review": request.form.get("review")
        }
        
                # insert the new review in my db
        mongo.db.reviews.insert_one(review)
        # display a message 
        flash("Review Successfully Added!")
    
    
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    
    reviews = mongo.db.reviews.find({"book": book['title'].lower()})
    return render_template("view_book.html", book=book, reviews = reviews)

# If this file is executed as the main script
if __name__ == "__main__":
    # Run the Flask application with the configuration from environment variables
    app.run(
        host=os.environ.get("IP"),  # Get the IP from environment variables
        port=int(os.environ.get("PORT")),  # Get the port from environment variables
        # Enable debug mode --> For the project, it should be set to False
        debug=True 
    )


