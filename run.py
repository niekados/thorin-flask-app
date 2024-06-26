import os
# Import json 
import json
# Import Flask class
from flask import Flask, render_template, request, flash
# Import env
if os.path.exists("env.py"):
    import env


# Create instance of this class
app = Flask(__name__)

# To use the secret key after we instantiate the app
app.secret_key = os.environ.get("SECRET_KEY")

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


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member) # first 'member' is the variable name being passed through into our html file. The second 'member' is the member object we created above.


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name"))) #It takes the 'name' key from our form, then using the .format() method, it injects that name into this particular flash message.
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__": # __main__ is name for default module in python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"), # using os to get IP environment variable if it exists, otherwise we set default value if it is not found
        port=int(os.environ.get("PORT", "5000")), # set it to integer and set default value to 5000
        debug=True) #specify "debug=True", because that will allow us to debug our code much easier during the development stage. NEVER have debug=True in production version!! Change to debug=False in final version