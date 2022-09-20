from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, IntegerField, FloatField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
from flask_wtf.file import FileField, FileAllowed, FileRequired


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class ProductUploadForm(FlaskForm):
    productname = StringField('Product Name', validators=[DataRequired()])
    producttype = SelectField('Product Type', choices=[('processor', 'Processor'), ('motherboard', 'Motherboard'), ('graphicscard', 'Graphics Card'), ('powersupply', 'Power Supply'), ('cabinet', 'Cabinet'), ('memory', 'Memory'), ('harddrive', 'Hard Drive'), ('ssd', 'SSD'), ('monitor', 'Monitor'), ('cooler', 'Cooler')], validators=[DataRequired()])
    productimage = FileField('Product Image', validators=[FileRequired(), FileAllowed(['jpg'], 'Images only!')])
    productcost = IntegerField('Product Cost', validators=[DataRequired(), NumberRange(min=1)])
    productquantity = IntegerField('Product Quantity', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit Product')