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
# https://flask.palletsprojects.com/en/2.0.x/config/#configuration-best-practices
# 
########################################################################

from flask import Flask, render_template
from form import ContactForm

app = Flask(__name__)

# Execute the following in a Python interpreter to generate a random
# secret key:
# >>> import secrets
# >>> secrets.token_hex(16)

# DO NOT HARD CODE YOUR SECRET KEY,
# for demonstration purposes only
app.secret_key = '2283fe9058fe7c38c1ca61c55c5540ed'

@app.route("/", methods=["GET", "POST"])
def contact_form():

    # instantiate form
    form = ContactForm()

    # validate form input on POST
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        return render_template('thank_you.html', name=name, email=email, message=message)

    return render_template('contact_form.html', form=form)

if __name__ == "__main__":
    app.run(host='::')
