#!/usr/bin/python3
"""A module containing all forms used in the app"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, Optional


class SignupForm(FlaskForm):
    """A class that defines the Signup form"""
    first_name = StringField(validators=[InputRequired(), Length(
        min=2, max=100)], render_kw={"placeholder": "First Name"})

    last_name = StringField(validators=[InputRequired(), Length(
        min=2, max=100)], render_kw={"placeholder": "Last Name"})

    email = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=100)], render_kw={"placeholder": "Password"})

    phone_no = StringField(validators=[InputRequired(), Length(
        min=8, max=100)], render_kw={"placeholder": "Phone Number"})  

    address = StringField(validators=[InputRequired(), Length(
        min=8, max=200)], render_kw={"placeholder": "State, Country"})   

    submit = SubmitField("Signup")


class LoginForm(FlaskForm):
    """A class that defines the Login form"""
    email = StringField(validators=[InputRequired(), Length(
        min=10, max=100)], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=8, max=100)], render_kw={"placeholder": "Password"})  

    submit = SubmitField("Login")