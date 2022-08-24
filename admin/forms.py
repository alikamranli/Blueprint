from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField,SubmitField,EmailField

class ProductForm(FlaskForm):
    brand=StringField('Brand')
    model=StringField('Model')
    description=StringField("Description")
    submit=SubmitField()

class CustomerForm(FlaskForm):
    name=StringField('CustomerName')
    email=EmailField('CustomerEmail')