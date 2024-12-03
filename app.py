from flask import Flask

app = Flask(__name__)  # Create a Flask application instance


@app.route('/')  # Default route for the home page
def hello_world():
    return '<h1>Hello World :)</h1>'  # Returning HTML content


@app.route('/greet')  # Another route to display a simple greeting
@app.route('/greet/<name>')  # A dynamic route that accepts a name
def greet(name=""):
    return f'<h1>Hello {name.capitalize()}!</h1>' if name else '<h1>Hello Stranger!</h1>'


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask development server
