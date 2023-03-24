from flask_wtf import FlaskForm
import wtforms as wf

from . import app
from .models import Position


def get_positions():
    with app.app_context():
        positions = Position.query.all()
        choices = []
        for position in positions:
            choices.append((position.id, position.name))
        return choices


class PositionForm(FlaskForm):
    name = wf.StringField(label="Позиция", validators=[
        wf.validators.DataRequired()
    ])
    department = wf.StringField(label="Отдел")
    wage = wf.IntegerField(label="Ставка заработной платы", validators=[
        wf.validators.DataRequired()
    ])

    def validate_wage(self,field):
        if field.data<0:
            raise wf.validators.ValidationError('Зарплата не может быть меньше нуля')


class EmployeeForm(FlaskForm):
    name = wf.StringField(label="Имя", validators=[
        wf.validators.DataRequired()
    ])
    inn = wf.StringField(label="ИНН паспорта клиента", validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=14, max=14)
    ])

    position_id = wf.SelectField(label="Позиция", validators=[
        wf.validators.DataRequired()
    ])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position_id.choices = get_positions()

    def validate_inn(self, field):
        if not field.data.startswith('1') and not field.data.startswith('2'):
            raise wf.validators.ValidationError('ИНН должен начинаться с 1 или с 2')

class UserForm(FlaskForm):
    username = wf.StringField(label="Логин пользователя", validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=8, max=24)
    ])
    password = wf.PasswordField(label="Пароль", validators=[
        wf.validators.DataRequired()
    ])
