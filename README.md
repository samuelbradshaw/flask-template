# Flask Template

This is a sample Python [Flask](https://palletsprojects.com/p/flask/) app with the following features:
* Folder structure that can accomodate medium-sized projects
* MySQL database connection
* Sample routes that serve Jinja templates
* Sample “utility” routes (robots.txt and error pages)
* Base Jinja template that provides a consistent page structure
* Sample CSS styles, including light/dark theming

This template has grown out of boilerplate code from several personal projects, including [SingPraises.net](https://singpraises.net) and [Scripture Tools](https://scripturetools.net). Although it’s been tailored to meet my own needs, I hope it will be useful to others.

## Set up the project locally

These instructions are for macOS (other systems may vary).

### Clone the git repository

1. Open Terminal.

2. Navigate to the folder where you want to download the project:
```
cd /path/to/folder
```
 
3. Clone the repository:
```
git clone https://github.com/samuelbradshaw/flask-template.git flask-template
```

If you prefer a GUI for git instead of Terminal, I recommend [Sourcetree](https://www.sourcetreeapp.com).

### Install Python 3 and MySQL (if needed)

Instructions for installing Python: [Installing Python 2 and 3 on macOS](https://gist.github.com/samuelbradshaw/932d48ef1eff07e288e25e4355dbce5d)

Instructions for installing MySQL: [Installing MySQL on macOS](https://gist.github.com/samuelbradshaw/2d435571fa0509f1bf732ecdd3e4f428)

### Set up a virtual environment for the project

1. Open Terminal and navigate to the project folder:
```
cd /path/to/project/folder
```

2. Set up and activate a virtual environment:
```
python3 -m venv .venv
source .venv/bin/activate
```

3. Install Flask and other Python dependencies in the virtual environment:
```
pip3 install -r requirements.txt
```

### Set up a local MySQL database

1. Log on to your MySQL instance. This can be done in Terminal, but I’d recommend using [Sequel Ace](https://apps.apple.com/us/app/sequel-ace/id1518036000?mt=12) as a GUI.
    * Host: `127.0.0.1`
    * Username: `[your-mysql-username]`
    * Password: `[your-mysql-username]`
    * Port: `3306`

2. Create a new database for the app to use (for example, `sample_database`).

### Create a project config file

1. Create a new Python file called config.py inside the `main` folder in the repository (this file isn’t tracked by git, because it contains configuration/credentials that are unique to the user).

2. Add the following lines to the config file, replacing the placeholders with your MySQL username, password, and database name:

```
SITE_NAME = 'Sample Website'

class DBInfo:
  SERVER = 'localhost'
  USERNAME = '[your-mysql-username]'
  PASSWORD = '[your-mysql-password]'
  DATABASE = '[your-database-name]'
  PORT = 3306
```

## Run the app

1. Navigate to the project folder and start the virtual environment (if it's not already running):
```
cd /path/to/project/folder
source .venv/bin/activate
```

2. Run the Python script that loads the site:
```
python3 run.py
```

3. Open the app in your browser:  
 http://127.0.0.1:8080
