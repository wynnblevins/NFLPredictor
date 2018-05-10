#!flask/bin/python
from flask import Flask, request
from predictor import runPredictor
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/winner')
def predictWinner():
    teamAId = request.args.get('teamAId', '')
    teamAName = request.args.get('teamAName', '')
    teamBId = request.args.get('teamBId', '')
    teamBName = request.args.get('teamBName', '')
    result = runPredictor(teamAId, teamAName, teamBId, teamBName)
    return result

if __name__ == '__main__':
    app.run(debug=True)