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

9. In our IDE terminal window 