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