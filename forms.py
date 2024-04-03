from wtforms import Form, StringField, SubmitField, DateField, IntegerField
from wtforms import validators
from wtforms.validators import InputRequired
from wtforms_alchemy import QuerySelectField

from model import Company


class ModelEditForm(Form):
    pattern = StringField("Информационный ресурс", validators=[
        validators.DataRequired(message="Поле обязательно для заполнения"),
        validators.Length(min=10, message="Длина должна быть от 10 символов")])

    sizes = IntegerField('Размеры', [validators.NumberRange(min=38, max=60)])
    consumption = IntegerField('Расход материала')
    pin = StringField("Код доступа", validators=[
        validators.DataRequired(message="Поле обязательно для заполнения"),
        validators.Length(min=10, max=10, message="Длина должна быть 10 символов")])


    button_save = SubmitField("Сохранить")
    button_delete = SubmitField("Удалить")

class JournalEditForm(Form):
    name = StringField("Название журнала", validators=[
        validators.DataRequired(message="Поле обязательно для заполнения"),
        validators.Length(min=3, max=50, message="Длина должна быть от 3 до 50 символов")])
    date_of_issue = DateField("Дата издания", validators=[
         InputRequired('Please enter a Start Date in format dd/mm/yyyy. E.g. 25/2/1999.')
         ], format = '%Y-%m-%d')

    pin = StringField("Код доступа", validators=[
        validators.DataRequired(message="Поле обязательно для заполнения"),
        validators.Length(min=10, max=10, message="Длина должна быть 10 символов")])

    button_save = SubmitField("Сохранить")
    button_delete = SubmitField("Удалить")

class CompanyEditForm(Form):
    name = StringField("Название компании", validators=[
        validators.DataRequired(message="Поле обязательно для заполнения"),
        validators.Length(min=3, max=50, message="Длина должна быть от 3 до 50 символов")])

    pin = StringField("Код доступа", validators=[
        validators.DataRequired(message="Поле обязательно для заполнения"),
        validators.Length(min=10, max=10, message="Длина должна быть 10 символов")])


    button_save = SubmitField("Сохранить")
    button_delete = SubmitField("Удалить")

class SearchForm(Form):
    name = StringField("Название компании",
        #                validators=[
        # validators.DataRequired(message="Поле обязательно для заполнения"),
        # validators.Length(min=3, max=50, message="Длина должна быть от 3 до 50 символов")]
                       )


    button_search = SubmitField("Сохранить")
