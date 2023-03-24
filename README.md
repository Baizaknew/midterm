# Midterm project
I decided to make a midterm project on the Flask framework, and for the final I will do it on Django.

**Flask** is a framework for building web applications using the Python programming language.
“Micro” doesn't mean that your entire web application fits into a single file of Python code, although it certainly could. Also, this does not mean that Flask lacks functionality. The "micro" in "microframework" means that Flask aims to stick to a simple yet extensible core. Flask won't decide many things for you, like which database to use. And the decisions it can make, such as which templating engine to use, are easy to change. Everything else is up to you, so Flask may turn out to be everything you need and nothing more.
## Description of the project "Application Flask for accounting employees in the office"

This project is a web application based on Flask for accounting employees in the office. The application uses a database to store information about employees and positions, and also allows users to log in and register.

### The application has the following functionality:

* creating, editing and deleting employees
* creating and editing positions
* registration, authorization and logout of users
* data validation when creating/editing employees and positions

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
* **app.py**  - the main file of the application, which contains all the routes and request processing functions
* **models.py**  - file with data models that are used in the application
* **forms.py**  - file with form classes used to create and validate user data
* **views.py** - file containing view functions (views)
* **urls.py** - file containing roots
* **templates**  - folder with HTML templates used to display application pages
* **static**  - folder with static files like images and stylesheets
* **migrations**  - directory with migrations for the database.
* **instance**  - directory with database

### Project functionality
#### Models
##### Position
Model for storing information about the position of an employee. Contains the following fields:
* id - position ID (auto-generated when creating a post).
* name - name of the job (string).
* department - the department to which the position belongs (string).
* wage - wage rate (integer value).

##### Employee
Model for storing information about an employee. Contains the following fields:
* id - employee ID (auto-generated when creating a record).
* name - employee's full name (string).
* inn - TIN of the employee's passport (string).
* position - connection to the Position model.
* position_id - employee position ID.

##### User
The user model contains the following fields:
* username - a column for storing the user's login (must be unique)
* password_hash - column for storing password hash

This class has a password property that is used to store data in password_hash.


#### Forms
Form classes created in forms.py file:

* PositionForm - a form for creating and editing a position
* EmployeeForm - a form for creating and editing an employee
* UserForm - a form for registering and authorizing a user

Each form contains the required fields to fill out, as well as validation for some fields:

* The wage field of the PositionForm class cannot have a negative value.
* The inn field of the EmployeeForm must start with either 1 or 2 and must be 14 characters in total.
* All other fields are required, except for the department field of the PositionForm.

####Functions
List of functions created in the views.py file:

* index is a function that uses index.html to display all Employees. Available at URL http://127.0.0.1:5000/. Represents information about each employee in the form of a table.
* position_create is a function to create a new position. Uses standard_form.html as html file. Available at URL http://127.0.0.1:5000/position/create. Upon successful save, a success message should appear.
* employee_create - creates a new employee and saves it to the database. Uses the standard_form.html template to display the employee creation form. If the entered TIN already exists in the database, displays the message "A customer with this TIN already exists". URL: http://127.0.0.1:5000/employee/create
* employee_delete - deletes an employee from the database. Uses the confirm_delete.html template to display a confirmation to delete an employee. URL: http://127.0.0.1:5000/employee/delete/<id>
* employee_update - updates an employee's data in the database. Uses the standard_form.html template to display an employee update form. URL: http://127.0.0.1:5000/employee/update/<id>
* register - registers a new user. Uses the user_form.html template to display the signup form. URL: http://127.0.0.1:5000/register
* login - authorizes the user. Uses the user_form.html template to display the login form. URL: http://127.0.0.1:5000/login
* logout - clears the user's authorization data. Uses the user_form.html template to display the logout form. URL: http://127.0.0.1:5000/logout
