from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username_sec = StringField("id астронавта", validators=[DataRequired()])
    password_sec = PasswordField("Пароль астронавта", validators=[DataRequired()])
    username_cap = StringField("id капитана", validators=[DataRequired()])
    password_cap = PasswordField("Пароль капитана", validators=[DataRequired()])
    submit = SubmitField("Войти")

class GaleryForm(FlaskForm):
    img_file = FileField("Добавить картинку", validators=[DataRequired()])
    submit = SubmitField("Отправить")