# Midterm project
## Description of the project "Application Flask for accounting employees in the office"

This project is a web application based on Flask for accounting employees in the office. The application uses a database to store information about employees and positions, and also allows users to log in and register.

### Installing and launching the application

To run the application, follow these steps:

1. Download archive with pre-prepared files.
2. Create a virtual environment and activate it 
```
python -m venv venv
. venv/bin/activate (для Linux/Mac)
venv\Scripts\activate (для Windows)
```

3. Install required packages:
```
pip install -r requirements.txt
```
4. Create database and migrations:
```
flask db init
flask db migrate
flask db upgrade
```
5. Run the application:
```
python manage.py
```
6. Go to the main page of the application: http://127.0.0.1:5000/

### Application structure
