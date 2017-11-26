'''
Created on Nov 26, 2017

@author: ray
'''
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField("What is your name?", validators=[Required()])
    submit = SubmitField('Submit')
