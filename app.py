from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',username=name)

# Create Custom error pages
# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(debug=True)