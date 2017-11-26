'''
Created on Nov 26, 2017

@author: ray
'''
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length

class LoginForm(Form):
    '''
    classdocs
    '''
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')
        