## Step 1

Create a folder for the project

## Step 2

Open in VS Code and open a terminal

## Step 3

Create a virtual environment for the project

    MAC OS: python3 -m venv venv
    Windows: python|py -m venv venv

## Step 4

Activate the virtual environment

    MAC OS: source venv/bin/activate
    Windows: .\venv\Scripts\activate

## Step 5

Install Django dependency

    MAC OS: pip3 install django
    Windows: pip install django

## Step 6

Run the startproject command to create the project settings
Both OS: django-admin startproject NAME_OF_PROJECT .
Note: replace NAME_OF_PROJECT with config or any other NAME_OF_PROJECT

    Expected Output: two folders and a single file called **manage.py**

## Step 7

Running the django project

    MAC OS: python3 manage.py runserver
    Windows: python|py manage.py runserver

## Creating a Superuser/ login

1. close server (Ctrl C)
2. py manage.py createsuperuser
3. enter username:
4. enter email:
5. enter password (will have to type twice)
"# 112-Django" 
"# 112-Django" 
