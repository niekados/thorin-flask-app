# Deploying project to Heroku

## Login and create new app

1. Login in to Heroku.
2. In Heroku main page click "New" button and select "Create new app" from drop down menu.
3. In "App name" input enter unique app name, choose a Region from drop down menu, in our case we will select Europe and click "Create app" button.
4. Once app is created page will load into app dashboard page.


## Installing the Heroku CLI (command line interface)

*We are now going to have a look at the Heroku command-line interface, or what's often called
the Heroku toolbelt.*

5. Go back to project IDE (Gitpod in our case).
6. In terminal type `npm install -g heroku` to install Heroku.
    - *'`npm`' stands for 'Node Package Manager', and the '`-g`' means that we want to install Heroku system-wide, or globally. 
    If we don't add the `-g`, then it will only install this within a directory called '`node_modules`' which is not what we want.*
7. Once installation is finished we can login to Heroku using command `heroku login -i` in our terminal.
8. Follow on screen instructions and enter your account details.
    - If you have MFA enebled, then you will need to use API key insted of password, to retrieve your API key:
        1. In Heroku webpage, click on your avatar and select "Account Settings".
        2. In "Manage Account page" scroll down to "API Key" section.
        3. Click "Reveal" button to display your API key. *(Do Not click the "Regenerate API key..." button!)*
        4. Copy the key and paste it in your IDE terminal instead of your password (you don't need to enter your password at all, API key is used as a password).

- Usefull commands:
    - `heroku apps` will list all apps that we have created.
    - `heroku apps:rename [NEW app Name] --app [Specify Name of App to be renamed / OLD APP NAME]` example: `heroku apps:rename my-app-2024 --app my-app-2018` 

## Linking our Git repository to Heroku

9. In our IDE terminal window check if our main branch is up to date `git status`, if there is any untracked files you can add them all with `git add -A` or `git add .` , followed by `git commit -m "Deployment to Heroku"`. 
    - If we type: `git remote -v`, this will give me verbose output about the remotes that we have.
10. On Heroku app page click "Settings" tab and in "App information" section and copy "Heroku git URL".
11. Back in our IDE terminal. To add another remote, we will type: `git remote add`, then a name for our remote,
which I will call '`heroku`', since '`origin`' is already taken by our instance of GitHub,
and then finally, just paste the Heroku Git URL.
    - *Now when we type `git remote -v` it gives me both the Heroku Git URL, as well as the original GitHub URL.*
    - *If we push now our code directly to Heroku by typing: `git push -u heroku main`. THIS GETS REJECTED!!! as  we get error message `!     No default language could be detected for this app.`*

## Adding requirements.txt file

*A `requirements.txt` file contains a list of the Python dependencies that our project needs in order to run successfully.
It's also how Heroku can detect what language we're using. That's the reason why our push to Heroku failed in the previous step.*

12. To create a `requirements.txt` file, in terminal type: `pip3 freeze --local > requirements.txt`.
13. Now add the new file to staging area by typing `git add -A` in terminal.
14. Then commit changes `git commit -m "Add requirements.txt"`
15. And finally push it to Heroku `git push -u heroku main`

## Create Procfile

*A Procfile is a Heroku-specific type of file that tells Heroku how to run our project.*

16. To create Procfile `echo web: python run.py > Procfile`
    - *It's important to note that the Procfile has a capital 'P', not a lowercase 'p', as this is the requirement for Heroku.
    What this line does, is tells Heroku that it's going to be a web process, and the command
    to run our application is 'python run.py', which is name of the Python file that we've created.*
17. Now we can push our Procfile to Heroku `git add Procfile` followed by `git commit -m "Add Procfile"` and `git push`.

- *When I refresh the app, you can see that it's successfully loading now, but we're not finished yet.
    Remember how we needed to create a `SECRET_KEY` in order to use the `flash()` function for messages?
    If I were to try and submit the contact form now, it would throw an error.
    This is because our `SECRET_KEY` is an environment variable within our `env.py` file, and that
    file is being ignored by Git from our `.gitignore` file, so Heroku cannot see it.*
    
- *Before we fix that, I just want to show you one very important page, that you will become
    quite familiar with during development.
    If we go back into Heroku, click on "More" in the top right-hand corner, and then click
    on "View Logs", then we can see the history of our most recent build.
    This is where you should come to check for any Application Errors.
    You can also access these logs in your Terminal by typing: `heroku logs --tail --app APP-NAME`,
    so for me, it would be: "thorin-flask-app".*

## Adding hidden environment variables, or Config Vars

18. Go to Heroku app dashboard and click "Settings" tab.
19. In "Config Vars" section click "Reveal Config Vars" button.
20. First add the `KEY` of `IP` and the `VALUE` of `0.0.0.0` and click "Add".
21. Next add `KEY` of `PORT` and the `VALUE` of `5000` and click "Add". 
    - *If you recall, these were set at the bottom of our `run.py` file to get the app running.*
22. Now we need to grab our `SECRET_KEY` variable from our hidden `env.py` file.
23. Copy `SECRET_KEY` to Heroku config Vars as `KEY` and the `VALUE` will be the second secret key string that we set there.
    - *Now we can click on "More" and "View Logs" once again.
    Everything is running just fine, but if we needed to, we could manually restart the build
    by clicking "More", and then "Restart all dynos".
    The dyno is the container that's actually running our application.
    Dynos will only run if the site is being viewed, but will go back to sleep after 30 minutes
    of inactivity.
    If you work on your Heroku app, then step away from your computer for some time, you'll
    notice that it takes a bit longer to reload the page.
    This is because the dynos are waking back up, and generating the app again out of hibernation.*

## Deploying from GitHub

*So even though that's working just fine now, sometimes you might want to disconnect
Heroku and set your app to automatically deploy from GitHub instead.*

24. Go back to Heroku and click on the "Deploy" tab.
25. In "Deployment method" section click "GitHub".
26. Bellow enter your GitHub repository name and click "Search".
27. Under the search bar your repository name should appear and we will press "Connect" button.
28. Next we will select "main" branch and click "Enable Automatic Deploys" button. 
29. Scroll down to "Manual deploy" section and click "Deploy Branch" button.
    - Our application has failed to build, and this is because our app is now reading the code
    from GitHub instead, but we haven't push our code to GitHub yet.
30. Back in our IDE Terminal. Let's remove Heroku git branch by typing `git remote rm heroku` (`rm` stands for remove and 'heroku' for the remote to be removed). If we type `git remote -v` we will see that only GitHub `origin` remote is left and `heroku` is gone.
31. Now we can add chnages to GitHub with `git add -A`, `git commit -m "Push to GitHub"` and pushing them with `git push origin main`.
32. We can go back to Heroku and click "Deploy Branch". Heroku starts building our app and once it's complete we get a message "Your app was successfully deployed."


### REMEMEBR 4 MAIN STEPS:
1. Create Heroku App
2. Connect Git remote
3. Add `requirements.txt`
4. Add `Procfile` file


