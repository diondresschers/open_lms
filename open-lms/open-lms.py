# Deze file is zelf gemaakt. Dit is de hoofd app.

from flask import Flask             # We are importing this `Flask`-class.
from flask import render_template   # De `render_template`-functie is om templates te gebruiken in Flask.
app = Flask(__name__)               # We are making an instanse called `app` of this `Flask`-class. With `__name__`, it is default Python and it knows where to look for static files and templates.

@app.route("/")                     # This is the route, this is a route decorator. The `route` is the method.
@app.route("/home")
def hello():                        # This is the function
    return render_template('home.html')
##    return("<h1>Hello World!</h1>")          # This will be returned

@app.route("/about")
def about():
    return render_template('about.html')
##    return("About page")

#if __name__ == "__main__":          # If we don't run this directly, but import than the __name__ will be something different, and then the Debug will not be set.
#    app.run(debug=True)             # Run Flask Debug. With this, you can also run this Flask directly via `python3 fopen-lms.py`


