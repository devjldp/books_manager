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

@app.route('/')
def test():
  return("HI world")





# If this file is executed as the main script
if __name__ == "__main__":
    # Run the Flask application with the configuration from environment variables
    app.run(
        host=os.environ.get("IP"),  # Get the IP from environment variables
        port=int(os.environ.get("PORT")),  # Get the port from environment variables
        # Enable debug mode --> For the project, it should be set to False
        debug=True 
    )
