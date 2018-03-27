from flask import Flask, render_template

# create the application object
app = Flask(__name__)

@app.route('/')
def home():
    """
        Landing page for the app, displays templates/index.html

    """
    test_string = "this is a test string being passed from app.py to index.html"
    return render_template('index.html', test_string=test_string)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
