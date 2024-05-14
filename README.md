# Lesson 1

## Install

1. `pip3 install flask`

2. `touch run.py` - create python file.
    - In Flask, the naming convention for our main file to run our application is usually `run.py` or `app.py`.

3. The first thing that we need to do is to import the Flask class.
    ```python
    from flask import Flask
    ```
4. Next, we need to create an instance of this class.
    Again, in Flask, the convention is that our variable is called 'app'.
    ```python
    # Create instance of this class
    app = Flask(__name__)
    ```
5. Then, we use the route decorator to tell Flask what URL should trigger the function that follows.
    I will create a function called "index", which just returns the string, "Hello, World".
```python
@app.route("/")
def index():
    return "Hello, World"
```

6. 


<span style="color:red;">
<strong>One thing to take note of, is that we should never have `debug=True` in a production application, or when we submit our projects for assessment.
This is very important, because having debug=True can allow arbitrary code to be run, and obviously this is a security flaw.
You should only have debug=True while testing your application in development mode, but change it to debug=False before you submit your project.
</strong>
</span>

## Summary 
So let's go through this and understand what's happening.
First, we're importing our Flask class.
We're then creating an instance of this and storing it in a variable called 'app'.
The first argument of the Flask class, is the name of the application's module - our package.
Since we're just using a single module, we can use __name__ which is a built-in Python variable.
Flask needs this so that it knows where to look for templates and static files.
We're then using the app.route decorator.
In Python, a decorator starts with the @ symbol, which is also called pie-notation.
Effectively, a decorator is a way of wrapping functions.
When we try to browse to the root directory, as indicated by the "/", then Flask triggers the index function underneath and returns the "Hello, World" text.
So far, this isn't enough to get our application running, so we need to add some extra functionality to do that.
We can "import os" from the standard Python library, and then we're going to reference this built-in variable and say that:
if name is equal to "main" (both wrapped in double underscores), then we're going to run our app with the following arguments.
The 'host' will be set to os.environ.get("IP"),
and I will set a default of "0.0.0.0".
We're using the os module from the standard library to get the 'IP' environment variable if it exists, but set a default value if it's not found.
It will be the same with 'PORT', but this time, we're casting it as an integer, and I will set that default to "5000", which is a common port used by Flask.
We also need to specify "debug=True", because that will allow us to debug our code much easier during the development stage.
The word 'main' wrapped in double-underscores (__main__) is the name of the default module in Python.

# Lesson 2

## render_template

`from flask import Flas, render_template`

and we can render html template
```python
@app.route("/")
def index():
    return render_template("index.html")
```

templates has to be stored in `templates` folder

# Lesson 3

index and about is also called a view 

```python
# @app.route (python decorator) def index or about etc. is also called a view

@app.route("/") #"/" stands for root directory, where it can find app file
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")
```

In order for our navigation links to work, we need use the Jinja templating method of url_for in order to call the appropriate functions.
The format for that is: double curly brackets (opening and closing), url_for, and then the name of our function goes inside of single quotes wrapped inside of parentheses.

```html
<ul>
    <li>
        <a href="{{ url_for('index') }}">  <!-- url_for( has to coresspond the views names ) -->
    </li>  
    <li>
        <a href="{{ url_for('about') }}">  <!-- url_for( has to coresspond the views names ) -->
    </li> 
</ul>  
```

When Flask sees these two opening curly brackets, it knows that what's actually inside of there, will be some code.
What we're doing is calling the url_for() function that looks up the view called 'index()' or the view called 'about()', and then injects some text, which is the actual root.

The names have to correspond to the views, so for now, that means our index() view and our about() view.

# Lesson 3

## Template inheritance

One of the beauties of using a framework like Flask or Django, is that they allow us to
reuse as much code as possible.
Let's create a base template that can act as our primary page.
I will duplicate the `index.html` file, and then rename the new copy to `base.html`.

```html
<!-- base.html -->
<body>
    <nav>
        <ul>
            <!-- url_for( has to coresspond the views names ) -->
            <li><a href="{{ url_for('index') }}">Home</a></li> 
            <li><a href="{{ url_for('about') }}">About</a></li>
            <li><a href="{{ url_for('contact') }}">Contact</a></li>
        </ul>
    </nav>
<!-- we choose the name of the block, in this case its called "content" -->
    {% block content %}
    {% endblock %}
</body>
```


In its place, I'll write the words {% block content %} wrapped inside of curly brackets
and percentage symbols.
On the next line, I'll do the same, but put the word 'endblock'.
What we're doing here is defining a block, or an area, that we can inject content into
from other pages.
The difference between the percent sign and the double curly bracket notation that we've
used before, is that the double curly brackets contain an 'expression', which is outputting
something either onto the screen, or in this case, into our href.
The curly bracket and percentage are for statements that control the flow of our template, such
as a for-loop, if-statement, or this block element.


Now that we have that done, let's go back into the index.html file.
I'm going to delete all of the code that I put above my `<h1>`, and all of the code that
I put below it.
We're then going to put in its place: {% extends "base.html" %} making sure 'base.html' is
inside of quotes, but the entire statement is wrapped in curly brackets and percentage
symbols.

```html
<!-- index.html -->
{% extends "base.html" %}
<!-- we choose the name of the block, in this case its called "content" -->
{% block content %} 
    <h1>Home Page</h1>
{% endblock %}

```

### summary
Essentially, when our `index.html` file loads, Flask inherits everything from the base template.
It then looks for a block element (which we called 'content') and injects that content
into it.
The word 'content' is just a word that we chose, but we could have called the block
anything, not just 'content'.
In fact, if we have multiple blocks on a page, that's exactly what we would do.
After saving the file, you can see I have a yellow squiggly line at the beginning of
the file, as well as a yellow exclamation mark on the file itself.
If I hover over this, you can see that the warning is: "Doctype must be declared first."
We don't need to worry about this warning, since the <!DOCTYPE> is actually being extended
from our base.html file, so we don't need to add it again.
When I refresh and go back to my Home Page, you can see that it displays just the same
as it was before.

# Lesson 4

I'm going to use the command `mkdir static`, which stands for 'make directory' and call
it `static`.
Static is often used to refer to files that don't change, such as JavaScript files, image
files, and our CSS files.

By now, you are probably used to calling this 'Assets' on your front-end projects.
**You will use static files an awful lot more when we start looking at Django.**
Now that we've created our static directory, let's `CD` into it, which stands for 'change
directory'.

Next, we will use the `wget` command and paste the link that we copied from the Start Bootstrap
site.
That will download the source files for us, and when I type `LS` to list the files, you
can see that I have a zip file now called 'gh-pages'.
To unzip that file, we can use the unzip command: `unzip gh-pages.zip`.


## CSS link in base.html

We need to add a link in the head to reference one of our CSS files.
The standard shortcut for this is `link:css` and then hit the tab key.
In the link href, I will do the same thing we did in the previous videos (and below),
by using the 'url_for' function.
This time, however, `url_for` is going to take two arguments.
The first argument is `static` wrapped inside of single-quotes, so that url_for knows to
look in the static directory.
To add a second argument, separate them with a comma, and now we'll target a specific file.
`Filename='css/clean-blog.min.css'`, making sure that the actual path to our file is wrapped
in single-quotes.

# Lesson 5

One of the greatest benefits of using frameworks, is the fact that we can actually
get server-side code to provide the frontend with data.
That's exactly what we're going to do in this video.
In run.py file.
In the return statement from my 'about' view, I'm going to add in an additional argument 'page_title'.
You can call this anything you want.
The value for my variable will simply be a string with the text 'About', so page_title="About"
wrapped inside of quotes to make it a string.
```python
@app.route("/about")
def about():
    return render_template("about.html", page_title="About")
```

To use this new variable, let's go to the `about.html` file, and remove the text between
the `<h2>` tags at the top.
I will replace that text with: `{{ page_title }}`
Remember, double curly brackets is an expression that's going to display something on the page.
In this case, the expression being passed through into my HTML file from python, will
be the '`page_title`' that we've just created for each view.

```html
{% extends "base.html" %}
{% block content %}
<h2>{{ page_title }}</h2>
```

# Lesson 6

I'm going to go back to the `run.py` file, and will add in
an additional argument to our '`about`' function.
This new example variable will have the name of: `list_of_numbers`, and I will set that list
to equal to `[1, 2, 3]`.
Notice this isn't a "string" this time, but a standard Python list.


```python
@app.route("/about") # This is the route
def about():    # This is the view
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])
```

 I will just switch over to the About page.
 `{{ list_of_numbers }}` I will save the file, and go back to the preview
We can now see that our list is displaying in the square brackets.
However, since this is a list, one of the beauties of frameworks is being able to iterate
over lists using a for-loop.

```html
{% extends "base.html" %}
{% block content %}

{{ list_of_numbers }}
```
*then it's replaced with:

To do that, we use the `{%` notation, because if you remember, that's for statements, not
for expressions.
This is called 'logic control'.
I will write a standard template for-loop: `{% for number in list_of_numbers %}`.
We always need to make sure to stop our for-loop by using the 'endfor' statement: `{% endfor %}`. 
That way the Jinja templating language knows
where the for-loop stops, and doesn't throw any unwanted errors.
Inside of the for-loop, I'd like to generate a `<p>`aragraph tag for each iteration.
To do this, within a `<p>`aragraph tag, let's add our new '`number`' variable into an expression
using the two curly brackets method.
By the way, the word '`number`' can be called anything, I'm just using the name of '`number`'
since we're iterating over a list of multiple numbers.
For example, if I had a list of countries, I could write something like 
`{% for country in countries %}`. This will generate a new variable called '`country`'
and iterate through a python list called '`countries`' plural.
Please note, it's bad practice and can cause errors if you use the same name for the variable
and the list itself, so don't write `{% for countries in countries %}`.
We now have a simple for-loop.
What it's doing, is iterating through the `list_of_numbers` from python, and then displaying
each '`number`' in a `<p>`aragraph tag on the screen.
Our for-loop has created three sets of `<p>`aragraph tags, and injected the value from our `list_of_numbers`,
into each one respectively.

```html
{% extends "base.html" %}
{% block content %}

{% for number in list_of_numbers %}
    <p>{{ number }}</p>
{% endfor %}

<h2>{{ page_title }}</h2>
```

# Lesson 7

It would be good if we could load all of this information from a file, and then display
it to the screen.
I will start by creating a new directory called '`data`'.
Within this folder, I will create a file called '`company.json`'.
This file is going to contain an array of objects.
Square brackets for the array, then curly brackets for our first object.
This object will have three keys.
`"Name"`, which I will set to Thorin Oakenshield.
`"Description"`, which will contain a brief biography about him.
And then `"image_source"`, which will contain a link to the image.
Since we already have the biography details, I will just grab that from my '`About`' page.

```json
[
    {
        "name": "Thorin Oakenshield",
        "description": "",
        "image_source": ""
    }
]
```

A couple of things that I should mention here: First, in order for it to be valid JSON data,
we cannot have any carriage returns or new lines - the entire value must be on a single
line.
Using the built-in formatter will not work unfortunately.
I find it easier to start from the bottom, and work my way up, bringing each of the lower
lines up one at a time.
Just click and drag the mouse from the beginning of the line, and release at the end of the
line above it, then hit the 'space' key.
I'll continue doing this for each of the lines, until I have everything on a single line.
The next item I want to point out, is that we need to remove any double quotes, and replace
them with single quotes.
As you can see here, the word "Oakenshield" is wrapped in double quotes, so I will just
change that to single quotes.
If we have double quotes, then it assumes we're finishing our string, and ignores the
rest.

```json
[
    {
        "name": "Thorin Oakenshield",
        // description is one single line, without any breaks
        "description": "Thorin II was born in TA 2746 to the Dwarf prince Thráin II in the city of the Lonely Mountain. Early in his youth, Thorin and the other Dwarves of the Lonely Mountain were forced to flee by the dragon Smaug, in TA 2770. While in exile, he quickly grew into a capable warrior. This was demonstrated at the Battle of Azanulbizar, near Moria, in TA 2799. He fought with one of the Dwarven armies beneath Moria's East-gate, and at some point in the battle, his shield broke, and, using an oaken tree branch found on the ground as a shield, he gained the epithet 'Oakenshield', which remained with him even in death.",
        "image_source": "https://static.wikia.nocookie.net/lotr/images/e/ec/1400193_695248260488487_320403599_o.jpg"
    }
]
```
Next, go back to the run.py file, and now we want Python to import the data.
To do that, we first need to import the JSON library, because we're going to be passing
the data that's coming in as JSON.
It's as simple as typing: import json.

```python
import os
# Import json 
import json
# Import Flask class
from flask import Flask, render_template
```

Then, within my '`about`' view, I will initialize an empty array or list called '`data`'.
We need to have Python open the JSON file in order to read it.
This is called a '`with`' block.
with `open("data/company.json", "r")` as json_data: Python is opening the JSON file as "read-only",
and assigning the contents of the file to a new variable we've created called j`son_data`.
We need to set our empty '`data`' list to equal the parsed JSON data that we've sent through.
`data = json.load(json_data)` We no longer need this example `list_of_numbers`,
so I will remove that. Finally, I will pass that list into my return statement, and call it '`company`'.
`company=data` This is assigning a new variable called '`company`'
that will be sent through to the HTML template, which is equal to the list of data it's loading
from the JSON file.

```python
@app.route("/about") # This is the route
def about():    # This is the view
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)
```

Let's head over to the About file, and first test to see if everything is being passed
through fine.
We no longer need the existing for-loop, but instead, I just want to view the entire contents
from my new '`company`' variable that's being passed through from Python.
Save those changes, then go to the preview and reload the page.
As you can see, we have an array, and we have our JSON data within the array.
You can see my key-value pairs: `name, description, and image_source`.
Since this an array, I can refer to it using standard Python notation.

```html
{% extends "base.html" %}
{% block content %}

{{ company }}

<h2>{{ page_title }}</h2>
```

I will add `[0]` to retrieve the first element out of the array (which is actually currently
the only one we have in our JSON file).
Next, I will add `["name"]` wrapped inside of a string, to get the name key from that first
element.

```html
{% extends "base.html" %}
{% block content %}

{{ company[0]["name"] }}

<h2>{{ page_title }}</h2>
```

# Lesson 8

We can now go back to our about.html file and remove the 'company' expression that we
added on the last video.

Then, scroll down and remove the second featurette that was added for Fili and Kili.
Delete the entire thing, including the closing `</div> `tag.
Now, above the featurette that we've added for Thorin, but below the basic information
paragraph about the company, I will add in a for-loop.
`{% for member in company %}` As a reminder, '`member`' could've been any
word I chose, and company is the list we created in the Python file.
Let's find the closing `</div>` for this featurette, and then add the required `{% endfor %}`.
Essentially, every time this loop is evaluated, the HTML that's within the for-loop, is going
to be injected into our template.

```html
{% for member in company %}

    <div class="row featurette">
        <div class="col-md-7">
            <h3>{{ member.name }}</h3>
            <p>{{ member.description }}</p>
        </div>
        <div class="col-md-5">
            <img src="{{ member.image_source }}" alt="" class="featurette-image image-responsive">
        </div>
    </div>

    <hr class="featurette-divider">

{% endfor %}
```

# Lesson 9

As we said , it would be nice if we could reverse the order of the images and
text for each subsequent row, just as we did in our initial setup.
We can actually do this quite easily, because when we create a for-loop using the Jinja
templating language, it also creates an object for us called '`loop`'.
That '`loop`' object has a property which is '`.index`'.
This shows us exactly which iteration of the loop we're on.
If I just put it in there as an expression and reload the page, you can see that the
first iteration, so number 1, is Thorin, and number 2 is Kili and Fili, and so on and so
forth, until the very end of the loop, which is the number 13 for Gandalf.

We can actually move this `loop.index` and put it into our `member.name <h3> `tags.
I will just add a 'dot' after the index number, to separate it from the member's name.
This now gives us a nice numbered list of all the members of Thorin's company.

But we can do more than this.
We can actually check this value, to see where we are in the for-loop itself.
What we are going to do, is put an if-statement.
Just like with for-loops, if-statements in our templates go between curly brackets and
`%` notation, because they are logic.
Immediately after the opening `.featurette` row, let's add: `{% if loop.index % 2 != 0 %}`. 
Then, I will add the `{% endif %}` line before
the closing `</div>` tag.
This is to let the Jinja templating language know where to stop the if-statement.


End result of adjusting the code to inject data from `data.json`

```html
{% for member in company %}

    <div class="row featurette">

        {% if loop.index % 2 != 0 %}

            <div class="col-md-7">
                <h3>{{ loop.index }}. {{ member.name }}</h3>
                <p>{{ member.description }}</p>
            </div>
            <div class="col-md-5">
                <img src="{{ member.image_source }}" alt="" class="featurette-image image-responsive">
            </div>

        {% else %}

        <div class="col-md-5">
            <img src="{{ member.image_source }}" alt="" class="featurette-image image-responsive">
        </div>
        <div class="col-md-7">
            <h3>{{ loop.index }}. {{ member.name }}</h3>
            <p>{{ member.description }}</p>
        </div>

        {% endif %}
    </div>
    
    {% if loop.index != loop.length %}

        <hr class="featurette-divider">

    {% endif %}

{% endfor %}
```

# Lesson 10

But what we would like to be able to do, is to click on the title, or the name of one
of the characters, and have it bring us to a page that displays more information about
them. Doing this also allows us to demonstrate some of the advanced routing features of Flask.

Let's start by going to our `about.html` file, and add a link into our `<h3>` tags where it
shows the `loop.index` and the `member.name`.
For the `href` path, let's type: `href="/about/{{ member.url }}"`.
We will create that `member.url` value very shortly.

We are going to create a new key and value in our `company.json` file.

The new key will be called: `"url"`, since our href is pointing to `member.url`.
I will assign the value of "thorin", in all lowercase letters.
For the next one, again, be sure to add a comma after `"image_source"`, but this time
it will be: `"url": "kili-and-fili"`.

```json
[
    {
      "name": "Thorin Oakenshield",
      "description": "Thorin II, also called the Oakenshield, King under the Mountain or the Mountain King, was the son of Thráin II, the older brother of Frerin and Dís, the grandson of King Thrór and the uncle of Fíli and Kíli. Thorin was best known for his deeds as leader of a company that infiltrated the lost Kingdom under the Mountain to take it back from Smaug and for leading an alliance of Men, Dwarves, and Elves in the Battle of the Five Armies.",
      "image_source": "https://static.wikia.nocookie.net/lotr/images/3/3f/ThorinBIG.jpg",
      "url": "thorin"
    }
]
```
Now we need to use some of the advanced routing features in Flask,
which means we have to go back to our `run.py` file, and create a new route and view.
We cannot just modify our existing `'/about'` route here, because that's for the page that
displays all of our members.
Instead, let's create a new route decorator: `@app.route("/about/<member_name>")`.
The angle brackets will pass in data from the URL path, into our view below, and I've
opted to call this parameter: `'member_name'`.
I will create the view for this, which is going to be: `about_member`.
That can now take `member_name` from above, as an argument.
Just to clarify, whenever we look at our `'about'` URL with something after it, that will be
passed into this view.
We'll now create an empty object called `'member'`, which we're going to use to store our data
in later.
Just as we did in our about view, we are going to open our `company.json` file for read-only
access, and refer to that as `json_data`.
We will then create another variable inside, where we pass the data that we've pulled through
and converted into JSON.

Next, we will iterate through that data array that we've just created.
I will just give the variable name of `'obj'`, which is just an abbreviation for 'object'.
`"for obj in data:"`.
Then we want to check if that object's url key from the file, is equal to the `member_name`
we've passed through from the URL path.
`if obj["url"] == member_name:` If they do match, then we want our empty `'member'`
object from line 24 to be equal to the object in this loop instance.
Just to demonstrate that, we are going to return some HTML, the same as we did in one
of our earlier videos.
For now, I will just `return "<h1>" + member["name"] + "</h1>"`.


```python
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return "<h1>" + member["name"] + "</h1>"
```


When we looked at the Jinja built-in filters on a previous video, two of the filters we
could've used are "`replace()`" and "`lower()`".
We could have just used the `member.name` in our href links, but added the `lower()` filter
to make everything lowercase, and the `replace()` filter to convert any spaces to minus symbols
for example.
We are not going to use this particular method on this project, but I would like to quickly
demonstrate what that would look like.
I'll make a copy of the entire line so we can keep the original for now.
Instead of `member.url`, I will use `member.name`.
I will start with the `replace()` filter, and I need to replace any 'space' with the minus
symbol.
Kili & Fili have an ampersand, so I will then `replace()` the ampersand with the actual word
'and'. Óin has a special character in his name,
so I'll copy that accented Ó, and replace it with a standard 'o'.
Then finally, let's convert the entire replacement to lowercase by using the `lower()` filter.
The reason I'm not going to use this method, is because if you try to test it out with
Thorin's link, you'll get an error.
This is because his full member.name is Thorin Oakenshield, but we've set `member.url` to just
'thorin'.
You would need to modify the Python functionality to look at the `member.name `instead of the
`member.url`, and also use the replace and lower methods there to get the function setup properly.
This was purely just to demonstrate some of the built-in Jinja filters that you could
use.

```html
        <div class="col-md-7">
            <!-- Original line -->
            <h3><a href="/about/{{ member.url }}">{{ loop.index }}. {{ member.name }}</a></h3>

            <!-- Modified example line to use replace() and lower() , witjout a need for "url" key in jason file -->
            <h3><a href="/about/{{ member.name|replace(' ', '-')|replace('&', 'and')|replace('Ó', 'O')|lower }}">{{ loop.index }}. {{ member.name }}</a></h3>

            <p>{{ member.description }}</p>
        </div>
```

That's all quite helpful, but it would be even better if we had a template that was
displaying this information.
In my '`templates`' directory, I will create a new file, and call it '`member.html`'.
We want this page to behave like the other template files, so we need to extend our `base.html`
template.

```html
<!-- member.html -->
{% extends "base.html" %}
{% block content %}
    <div class="row">
        <div class="col-md-5">
            <img src="{{ member.image_source }}" alt="Profile image for {{ member.name }}">
            <h2 class="col-md-7">{{member.name}}</h2>
        </div>
    </div>

    <div class="col-md-12">
        <p>{{ member.description }}</p>
    </div>
{% endblock %}
```

Our HTML file is now created to provide basic information about the member when we click
on them.

We now need to go back into our `run.py` file.
Instead of returning hard-coded HTML, I will "`return render_template`".
The first argument is going to be our new `"member.html"` template that we just created.
The second argument will be "`member=member`".
This first '`member`' is the variable name being passed through into our html file.
The second '`member`' is the member object we created above on line 24.
Okay, so we can save that, and now when I reload the preview, then click on Thorin,
as we can see, it's extending the `base.html` template, and I have all of the basic information
about Thorin from our JSON file.

```python
@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)
```

# Lesson 11

## Contact form

We are going to use an HTTP method.
Within our `form` element, we need to add `method="POST"`.
Remember that we've looked at HTTP methods before.
The `GET` method is used for retrieving data from the server, whereas the `POST` method is
used for sending data to the server.
What we also need to do, is give each of our `<input> `elements a `name` attritube.
It's usually best to have the `name` match the `id`, so within the `<input>` field for someone's
'`Name`', I will add: `name="name"`, since the `id="name"` as well.

When I click on 'Send' now, I get an error: "Method Not Allowed".
You can also see that it's a 405 Method Not Allowed error on the page tab as well, so
this is an error from our server.
If I go back and have a look inside of the Terminal, you can see that I have a red POST
error, with a response of 405 from the server.
The reason this is happening, is because by default, all of Flask's views will handle
a `GET` request.
If we need to start handling anything outside of that, such as `POST`, or the other methods,
`DELETE` or `PUT`, then we need to explicitly state that our route can accept those methods.

Within the `run.py` file, we need to go to our '`contact`' route, and we will add in another
argument.
After the URL path of '`/contact`', I will add a comma, followed by: `methods=["GET", "POST"]`.
Even if we only have a single method for `POST`, the list variable still needs to be called
'`methods`'.

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html", page_title="Contact")
```

Now we are no longer getting an error 405, but again, we also don't get anything back.
So how exactly do we know that it's actually working?
Well, one of the ways is by having a look at the debugger in the Terminal.
You'll notice my previous request of posting the contact form resulted in a 405 error,
which was that the method was not allowed.
This time when we did it, we got a 200 response code, and as we remember before, the 200 response
code means "that's okay, everything worked fine".

```terminal
<!-- Before in terminal -->
[14/May/2024 20:09:52] "POST /contact HTTP/1.1" 405 -
<!-- Now in terminal -->
[14/May/2024 20:18:57] "POST /contact HTTP/1.1" 200 -
```

We can actually do something with that data now.
The first thing we need to do, is import the '`request`' library from Flask.
Request is going to handle things like finding out what method we used, and it will also
contain our form object when we've posted it.
Within our contact view, we'll just add in an '`if-statement`', and we are going to use
the '`method`' of the '`request`' object: `if request.method == "POST":`

```python
# Top of run.py file
from flask import Flask, render_template, request
# Contact view
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
    return render_template("contact.html", page_title="Contact")
```

The request object has a lot more things attached to it as well.
When we submit a form, it actually has the form-object attached.
Remember that we gave each of our form elements the name attribute?
Let's see what happens if we print "`request.form`".
Once again, save that, go back to our contact form, and I will add more test data into the
form, and click on send.
In the terminal debugger, you can see that we have this thing called an '`ImmutableMultiDictionary`'.
But there it is, we have the data that came through from our form.
My name, email address, phone number, and a message, all being passed through our `POST`
method with a status code of `200`, so it worked!
Because this is a dictionary, we can actually use a standard Python method of accessing
the keys for that dictionary.
If I `print(request.form.get("name"))`, this will allow us to get the '`name`' value from
our form.
Back within the debugger, it's printed out just the value of the name input,
using `request.form.get('name')`.


I want to quickly show you another way to do the same thing.
Instead of `request.form.get`, I will make a copy of this and use: `request.form['email']`
but this time inside of square brackets, and not using the `.get() method`.
I'll resubmit the form once again, and then see what gets returned into the debugger now.
By using `.get()`, if the form doesn't actually have a key of '`name`' or `'email`' for example,
then it would display '`None`' by default.
However, by just using `request.form[]`, if there isn't a '`name`' or '`email`' key on our
form, instead of returning '`None`', it would throw an exception.
That's how we can access a form's data from the backend of our site.

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Original get method
        print(request.form.get("name"))
        # Square bracket get request
        print(request.form["email"])
    return render_template("contact.html", page_title="Contact")
```

```python
# If there isn't such key in doctionary we would get
    request.form.get("key")  # = None

    request.form["key"] # = Exception
```

# Lesson 12

## Form submit feedback

Now that we have information coming from our form, we can do stuff with it on the backend.
What we want to do next, is display some feedback to the user.
To do that, we are going to import a function from Flask called '`flash`'.

```python
from flask import Flask, render_template, request, flash
```

Sometimes we want to display a non-permanent message to the user, something that only stays
on screen until we refresh the page, or go to a different one.
These are called '`flashed messages`' in Flask.
We want to display a flashed message when our visitor submits the contact form.
To use flashed messages, we need to create a secret key, because Flask cryptographically
signs all of the messages for security purposes.
This might sound complicated, but really, all we need to do is provide a secret key
that Flask can use to sign the messages.
Generally, in production mode, we would keep the secret key private, so let's take a look
at how to do that.


First, I need a new Terminal opened.

The first thing we need to do is create a new file called "`.gitignore`".
Any file or folder that we add to this, will be ignored by GitHub, so we don't accidentally
commit files that contain sensitive data.
I will type: '`touch .gitignore`'.
Next, we want to create a file called: "`env.py`", so let's type: '`touch env.py`'.
This is where were will hide any sensitive data or environment variables that shouldn't
be pushed to GitHub for example.
Within the `env.py` file, we will import the `os` library from Python.
We can now use the operating system method called '`environ`', short for environment variable
as an example.
We want to set a hidden variable, so let's type: `os.environ.setdefault()`.
This will take two aruments.
The first is our variable name that will be used to grab the confidential data, which
I shall call "`SECRET_KEY`".
The second is the key itself, whether it's an API key for example, or confidential database
information which we'll see later.
We need to separate these with a comma, and for now, I will assign my `SECRET_KEY` the value
of: '`secret_flash_key`'.
You can make this secret key anything you'd like, as long as it's hidden and is a string.

```python
#env.py
import os
os.environ.setdefault("SECRET_KEY", "secret_flash_key")
```

Next, we'll go to our `.gitignore` file.
We need to tell GitHub to ignore the '`env.py`' file when we make any commits to the repository,
so I will type '`env.py`' and save it.

Now we can go back to our `run.py` file, and below our imports at the top, we just need
to import one more library, called '`env`'.
But, we only want to import `env`, if the system can find an `env.py` file.
`if os.path.exists("env.py"): import env`

```python
import os
# Import json 
import json
# Import Flask class
from flask import Flask, render_template, request, flash
# Import env
if os.path.exists("env.py"):
    import env
```

Once we save that, a new directory called '`pycache`' is created.
We don't need to bother pushing that to GitHub either, so let's go back into our `.gitignore`
file and type: `__pycache__/`.
The '`/`' at the end identifies it as a directory, and so will therefore ignore everything within
that folder as well.

We now want to grab the hidden variable, which we've called `SECRET_KEY`.
To use it, after we instantiate our app, we need to write: `app.secret_key = os.environ.get("SECRET_KEY")`.

```python
# To use the secret key after we instantiate the app
app.secret_key = os.environ.get("SECRET_KEY")
```

Below, within our contact view, instead of the `print` statements, I'm going to call the
`Flash()` function.
`flash("Thanks {}, we have received your message!".format(request.form.get("name")))`.
Once I save that, you can see a `red error `underneath `.get()`, so if I hover over that,
it says `"Line Too Long"`.
This is from an extension I'm using, and essentially says that lines should not be greater than
79 characters long in order to be `PEP8 compliant`.
You can see in the bottom of my IDE, it tells me that my cursor is currently on line 39,
at the 92nd character for that line.
<span style="color: red;">There are a few ways to fix this 'line too long' error for PEP8 compliance, but the easiest
is to just hit enter after any opening-parentheses symbol.</span>
That will ensure that it's at the correct tab location on the next line as well.

```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")
```

All we need to do now is update our contact template, so that it can retrieve the flashed
messages.
To do that, we are simply going to create a `{% with %}` block, similar to if/else statements
or for-loops.
Above the form, just inside of the first column, I will type: `{% with messages = get_flashed_messages() %}`. 
`get_flashed_messages()` will return any of
the messages that we've created using the `Flash()` function on the backend, and store
that in a variable called messages.
We need to close our `{% endwith %}` as well.
Next, we are going to check if there are any messages to retrieve.
`{% if messages %}` Let's also just close our `{% endif %}` here
as well. If we have successfully returned any messages from our `get_flashed_messages()` function,
then we are going to create some HTML.
I want to display each message within an unordered list, so I can build that using a class name of 'flashes' that we can style later if we wanted to.
Inside of our `<ul>`, we want to iterate through each of the messages, because it's possible
for us to receive more than one from the backend on a single page.
`{% for message in messages %}`. Don't forget to close that for-loop using:
`{% endfor %}`. Finally, for each message, we will insert
a line item: `<li>{{ message }}</li>`.

When we reload our live preview, and resubmit the form, you can see here now, our flash
message is displayed as a bullet-point list item: "Thanks Tim Nelson, we have received
your message!"  [ its part of HTML and not a pop up alert style message ]

```html
<div class="row">
    <div class="col-lg-8 col-md-10 mx-auto">

        <!-- get_flashed_messages() will return any of messages we created using flash() function -->
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul class="flashes">
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}

        <p>Want to get in touch? Fill out the form below to send me a message and I will get back to you as soon as
            possible!</p>
        <form method="POST" name="sentMessage" id="contactForm" novalidate>
```

