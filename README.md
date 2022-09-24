# Django Introduction

A walkthrough project from the Code Institute for the level 5 diploma in web application development - Introduction to Django.

## Initial Setup of the project
### Using VSCode

1. Create your repository on GitHub and clone the repository into VSCode using SSH.
2. Create a .venv folder in the root directory. This will be used when we create a virtual environment using pipenv and stores all files and folders relating to the virtual environment.
3. Create a .gitignore file in the root directory. The .gitignore file is where you will list all files and folders that you do not want to be tracked, which will prevent them from being pushed to GitHub. This is really important for projects that contain sensitive data such as environment variables that include keys which should be kept private.

### Virtual Environments and installing Django

For this project I will be using pipenv to create a virtual environment and to install packages.

1. Install Django. For the Code Institute walkthrough it is important to install Django version 3.2. This is the long term support (LTS) version of Django which makes it preferable to use over the newest version of Django.

``` bash
pipenv install django==3.2
```

2. A pop-up will ask whether you want to create the virtual environment for the current workspace - click yes.
3. To launch the virtual environment we will then need to run:

``` bash
pipenv shell
```

Once this is complete you will see that there are files and folders in the .venv file and a `pipfile` and `pipfile.lock` in the root. The pipfile is similar to requirements.txt, it lists all the packages installed. You should not make any changes in `pipfile.lock` as this can cause errors.

### Creating a Django project

Django comes with a built in admin command we can use to create our project:

``` bash
django-admin startproject PROJECT_NAME .
```

Change the PROJECT_NAME to the name of the project. The dot at the end of the command lets Django know we want to create the project in the current directory.

This will then create two new items, the project directory folder `django_todo` and a `manage.py` file. The project directory will hold:

* `__init.py` - this file tells the project that this is a directory we can import from
* `settings.py` - holds all the global settings for the entire project (e.g. debug settings, where the HTML templates are located and what database to connect to)
* `urls.py` - contains the routing information which allows a user to type a specific URL into their address bar and hit a specific python function (similar to app.route in flask)
* `wsgi.py` - contains the code that allows the web server to communicate with the python application

### Running the project

We can run the project using  `manage.py`:

``` bash
python3 manage.py runserver
```

There will be a link in the terminal for the development server. To open it hold `command` + click. A brower tab will open and you should see a message letting you know the install was successful.

---
