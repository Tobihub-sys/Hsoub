# Import the Flask class from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def index():
    # Render the HTML template
    return render_template('index.html')

# Run the application if the script is executed
if __name__ == '__main__':
    app.run(debug=True)
