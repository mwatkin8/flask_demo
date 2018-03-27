from flask import Flask, render_template
import db_functions

# create the application object
app = Flask(__name__)

@app.route('/')
def home():
    """
        Landing page for the app, displays templates/index.html

    """
    test_string = "this is a test string being passed from app.py to index.html"
    return render_template('index.html', test_string=test_string)

@app.route('/db')
def make_db():
    db_name = "therapy.db"
    patient = db_functions.run(db_name)
    return render_template('index.html',patient=patient)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
