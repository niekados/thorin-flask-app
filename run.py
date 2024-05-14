import os
# Import json 
import json
# Import Flask class
from flask import Flask, render_template


# Create instance of this class
app = Flask(__name__)

# @app.route (python decorator) def index or about etc. is also called a view

@app.route("/") #"/" stands for root directory, where it can find app file
def index():
    return render_template("index.html")


# pep8 compliance- has to be seperted by two blank lines between views
@app.route("/about") # This is the route
def about():    # This is the view
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__": # __main__ is name for default module in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # using os to get IP environment variable if it exists, otherwise we set default value if it is not found
        port=int(os.environ.get("PORT", "5000")), # set it to integer and set default value to 5000
        debug=True) #specify "debug=True", because that will allow us to debug our code much easier during the development stage. NEVER have debug=True in production version!! Change to debug=False in final version