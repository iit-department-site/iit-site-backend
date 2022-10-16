
# Ai site 

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

This is backend part of AI site.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.
First install virtual environment
```
pip install virtualenv
```
Creation of a virtual environment
```
virtualenv venv 
```
Activating the virtual environment
```
.\venv\Scripts\activate win
```
linux
```
source mypython/bin/activate 
```
installing dependencies
```
pip install -r requirements.txt
```

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be
```
cd ai_site
```
To migrate the database
```
python manage.py makemigrations 
```
```
python manage.py migrate
```
To create a admin user:

```
python manage.py createsuperuser
```
And to run the server:
```
python manage.py runserver
```

## Usage <a name = "usage"></a>
Add notes about how to use the system:
* Django
* Postgres

