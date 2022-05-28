########################################################################
# Simple contact form example
#
# This script was written for the Victoria Raspberry PiMakers And Others
# Meetup Group presentation on May 27, 2022.
#
# Gordon M. Celesta
# gordo@sdf.lonestar.org
#
# INSPIRED BY
#
# https://www.geeksforgeeks.org/create-contact-us-using-wtforms-in-flask/
#
# FURTHER READING
#
# Defining forms
# https://wtforms.readthedocs.io/en/2.3.x/forms/#defining-forms
#
# Validators
# https://wtforms.readthedocs.io/en/2.3.x/validators/
#
########################################################################

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

# Define the form with validators
class ContactForm(FlaskForm):
    name = StringField(label='Name',
                       validators=[DataRequired()])
    email = StringField(label='Email',
                        validators=[DataRequired(),
                        Email(granular_message=True)])
    message = TextAreaField(label='Message',
                            validators=[DataRequired()])
    submit = SubmitField(label="Send")
