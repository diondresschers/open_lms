# Deze file is zelf gemaakt. Dit is de hoofd app.

from flask import Flask             # We are importing this `Flask`-class.
from flask import render_template   # De `render_template`-functie is om templates te gebruiken in Flask.
app = Flask(__name__)               # We are making an instanse called `app` of this `Flask`-class. With `__name__`, it is default Python and it knows where to look for static files and templates.

# Dit wordt wat dummy data, aangezien we nog geen database hebben.
posts = [
    {
        'author' : 'Dion Dresschers',
        'title' : 'Blog Post 1',
        'content' : 'Eerste bericht',
        'date_posted': '2021-03-08',
    },
    {
        'author' : 'Henk Heemstede',
        'title' : 'Blog Twee',
        'content' : 'Hier staat info in bericht',
        'date_posted': '2021-03-09',
    }
]

@app.route("/")                     # This is the route, this is a route decorator. The `route` is the method.
@app.route("/home")    
def hello():                        # This is the function
    return render_template('home.html', posts=posts, title="ja een titelatuur!")            # De eerste `posts` wordt gebruikt in de Jinja2 template, de tweede `posts`, is de posts variabele hierboven. # De `title` is ook zelfgekozen en wordt gebruikt in de Jinja2 als `title`.
##    return("<h1>Hello World!</h1>")          # This will be returned

@app.route("/about")
def about():
    return render_template('about.html', title="ABOUT!")
##    return("About page")

#if __name__ == "__main__":          # If we don't run this directly, but import than the __name__ will be something different, and then the Debug will not be set.
#    app.run(debug=True)             # Run Flask Debug. With this, you can also run this Flask directly via `python3 fopen-lms.py`


