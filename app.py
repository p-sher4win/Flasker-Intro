from flask import Flask, render_template, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

# Secret Key
app.config['SECRET_KEY'] = "my super secret key that no one is suppose to know"

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name", validators=[DataRequired()])
    submit = SubmitField("Submit")

@app.route('/')
def index():
    first_name = "John"
    stuff = "This is <strong>Bold</strong> text"
    stuff2 = "This is title text"
    pizza = ["Chicken", "Mushroom", "Sausage", 19]
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           stuff2=stuff2,
                           pizza=pizza)

@app.route('/user/<username>')
def user(username):
    return render_template('user.html',username=username)

# Create Custom error pages
# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()

    # Validate form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successful")

    return render_template('name.html',
                           name=name,
                           form=form)


if __name__ == "__main__":
    app.run(debug=True)