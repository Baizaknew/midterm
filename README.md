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
![Screenshot_26](https://user-images.githubusercontent.com/102854080/227507713-5399b090-ebd4-4478-856a-3a8e5a3ea83d.png)


#### Forms
Form classes created in forms.py file:

* PositionForm - a form for creating and editing a position
* EmployeeForm - a form for creating and editing an employee
* UserForm - a form for registering and authorizing a user

Each form contains the required fields to fill out, as well as validation for some fields:

* The wage field of the PositionForm class cannot have a negative value.
![Screenshot_25](https://user-images.githubusercontent.com/102854080/227507186-ed1ff4ae-0e80-4a73-9b98-c637732f74d0.png)
* The inn field of the EmployeeForm must start with either 1 or 2 and must be 14 characters in total.
![Screenshot_23](https://user-images.githubusercontent.com/102854080/227506336-015663f5-7d8d-42ff-961e-e75a6263459f.png)
![Screenshot_24](https://user-images.githubusercontent.com/102854080/227506782-44fa0eba-84ec-47b4-835c-2f728baf36c7.png)
* All other fields are required, except for the department field of the PositionForm.

####Functions
List of functions created in the views.py file:

* register - registers a new user. Uses the user_form.html template to display the signup form. URL: http://127.0.0.1:5000/register
![Screenshot_25](https://user-images.githubusercontent.com/102854080/227502825-ca40a828-67f5-4917-a458-6e96586943b3.png)
* login - authorizes the user. Uses the user_form.html template to display the login form. URL: http://127.0.0.1:5000/login
![Screenshot_18](https://user-images.githubusercontent.com/102854080/227502979-81cf8845-cc21-4db3-8cba-383cc984f29c.png)
* index is a function that uses index.html to display all Employees. Available at URL http://127.0.0.1:5000/. Represents information about each employee in the form of a table.
![Screenshot_20](https://user-images.githubusercontent.com/102854080/227502229-665a54bc-ad4d-43e9-911e-84f36c0610d0.png)
And you can see that our login with which we logged in appeared at the bottom of the site:
![Screenshot_26](https://user-images.githubusercontent.com/102854080/227503489-5940d412-e48a-4266-976a-f3c168e9fd49.png)
So if you are logged in, you can see additional cells (Change, Delete).
![Screenshot_28](https://user-images.githubusercontent.com/102854080/227504831-89115502-9add-49ef-b532-698ed9583712.png)
And if you are not logged in, then you will not see these cells.
*******************************************************************************************
* position_create is a function to create a new position. Uses standard_form.html as html file. Available at URL http://127.0.0.1:5000/position/create. Upon successful save, a success message should appear.
![Screenshot_20](https://user-images.githubusercontent.com/102854080/227505344-55be7af2-f83f-4627-a119-9b312d1f4c05.png)
* employee_create - creates a new employee and saves it to the database. Uses the standard_form.html template to display the employee creation form. If the entered TIN already exists in the database, displays the message "A customer with this TIN already exists". URL: http://127.0.0.1:5000/employee/create
![Screenshot_18](https://user-images.githubusercontent.com/102854080/227505258-ea6d4e30-57cf-4901-98a6-14821b4aea8d.png)
* employee_delete - deletes an employee from the database. Uses the confirm_delete.html template to display a confirmation to delete an employee. URL: http://127.0.0.1:5000/employee/delete/<id>
![Screenshot_21](https://user-images.githubusercontent.com/102854080/227505994-262a8cd7-7aaa-43bf-b74a-474d91bf2150.png)
* employee_update - updates an employee's data in the database. Uses the standard_form.html template to display an employee update form. URL: http://127.0.0.1:5000/employee/update/<id>
![Screenshot_22](https://user-images.githubusercontent.com/102854080/227506025-6b34142e-6f45-46af-b9d3-f261bf621df7.png)
* logout - clears the user's authorization data. Uses the user_form.html template to display the logout form. URL: http://127.0.0.1:5000/logout

### Database schema (ERD image)

![Screenshot_27](https://user-images.githubusercontent.com/102854080/227513900-a779f417-f453-4d34-9c9f-1fb6404cf8ab.png)
* The Position table has a one-to-many relationship with the Employee table. Each position can have multiple employees, but each employee can only have one position.
* The Employee table has a many-to-one relationship with the Position table. Each employee must have a position, but a position can have no employees.
* The Employee table also has a one-to-one relationship with the User table. Each employee must have a corresponding user account, but a user account can be associated with only one employee.
* The User table has a one-to-one relationship with the Employee table. Each user account must be associated with an employee, but an employee does not necessarily have to have a user account.