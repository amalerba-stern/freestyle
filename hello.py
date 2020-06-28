# hello.py (root dir of repo)

from flask import Flask

app = Flask(__name__)

# route: a URL path to visit
# route function names should be unique hello_world() vs about()

@app.route("/")
def hello_world():
    print("VISITED THE HELLO PAGE")
    return "Hello, World!"

@app.route("/about")
def about():
    print("VISITED THE ABOUT PAGE")
    return "About me!"