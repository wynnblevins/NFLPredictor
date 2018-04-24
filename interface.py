#!flask/bin/python
from flask import Flask
from predictor import runPredictor

app = Flask(__name__)

@app.route('/winner')
def index():
    return runPredictor()

if __name__ == '__main__':
    app.run(debug=True)