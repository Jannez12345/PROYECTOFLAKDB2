from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class PersonaForm(FlaskForm):
    id = IntegerField('Id', validators=[DataRequired()])
    nombre=StringField('Nombre', validators=[DataRequired()])
    apellido = StringField('Apellido', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
