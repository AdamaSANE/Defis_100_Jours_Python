from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Greeting route
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)