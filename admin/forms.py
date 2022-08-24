from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,TextAreaField
class ProductForm(FlaskForm):
    name=StringField('Name')
    price=StringField('Price')
    amount=StringField("Amount")
    info=TextAreaField('Info')