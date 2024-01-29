
"""My Flask app."""

from flask import Flask, render_template, request, redirect, url_for    # Import Flask to allow us to create our app

"""__name__ is a special variable in Python that is automatically set to the name of the module in which it is used.
If the source script is executed as the main program, __name__ is set to '__main__'. 
If the module is imported from another module, __name__ will be set to the module's name."""

flask_app = Flask(__name__)    # Create a new instance of the Flask class called "flask_app"

# The "@" symbol designates a "decorator" which attaches the following function to the '/' route.
@flask_app.route('/')
def hello(): # The function associated with the route() decorator is called a "view function". We can use any
    # return render_template('index.html')    # Return the string 'Hello World!' as a response.
    # return render_template('index.html', name="Jay")
    # return render_template('index.html', name="Jay", phrase="Hello", times=5)    # Return the string 'Hello World!' as a response.
    return "<b>This is My Test WebApp with Flask</b>"
