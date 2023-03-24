from . import app

from .views import index, position_create, employee_create, employee_delete, \
    employee_update, register, login, logout

app.add_url_rule('/', view_func=index)
app.add_url_rule('/employee/create', view_func=employee_create, methods=['GET', 'POST'])
app.add_url_rule('/employee/<int:id>/update', view_func=employee_update, methods=['GET', 'POST'])
app.add_url_rule('/employee/<int:id>/delete', view_func=employee_delete, methods=['GET', 'POST'])

app.add_url_rule('/position/create', view_func=position_create, methods=['GET', 'POST'])

app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout)
