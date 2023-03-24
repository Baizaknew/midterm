from flask import redirect, render_template, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError

from . import app, db
from .models import Employee, Position, User
from .forms import EmployeeForm, PositionForm, UserForm


def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)


@login_required
def position_create():
    form = PositionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            position = Position()
            form.populate_obj(position)
            db.session.add(position)
            db.session.commit()
            flash(f'Успешно', 'success')
        else:
            flash(f'Ошибка', 'danger')
    return render_template('standard_form.html', form=form)


@login_required
def employee_create():
    form = EmployeeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            employee = Employee()
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash(f'Успешно', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Ошибка', 'danger')
    return render_template('standard_form.html', form=form)


@login_required
def employee_update(id):
    employee = Employee.query.get(id)
    form = EmployeeForm(obj=employee)
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(employee)
            db.session.add(employee)
            db.session.commit()
            flash(f"УРА! У вас получилось что-то поменять!", 'success')
            return redirect(url_for('index'))
        else:
            print(form.errors)
    return render_template('standard_form.html', form=form, employee=employee)


@login_required
def employee_delete(id):
    employee = Employee.query.get(id)
    form = EmployeeForm(request.form)
    if request.method == 'POST':
        db.session.delete(employee)
        db.session.commit()
        flash(f'Работник под номером {employee.id} успешно удален', 'danger')
        return redirect(url_for('index'))
    return render_template('confirm_delete.html', employee=employee, form=form)


def register():
    title = "Регистрация"
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User()
            form.populate_obj(user)

            db.session.add(user)
            try:
                db.session.commit()
            except IntegrityError:
                flash('Такой пользователь уже существует', "danger")
                return render_template('register.html', form=form, title=title)
            else:
                flash("Успешная регистрация", "success")
                return redirect(url_for('login'))
        else:
            print(form.errors)
    return render_template('user_form.html', form=form, title=title)


def login():
    title = 'Авторизация'
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash('Неправильные данные', 'danger')
                print(form.errors)
        else:
            print(form.errors)
    return render_template('user_form.html', form=form, title=title)


def logout():
    logout_user()
    return redirect(url_for('login'))

