#!flask/bin/python
from flask import Flask, request
from predictor import runPredictor

app = Flask(__name__)

@app.route('/winner')
def predictWinner():
    teamAId = request.args.get('teamAId', '')
    teamAName = request.args.get('teamAName', '')
    teamBId = request.args.get('teamBId', '')
    teamBName = request.args.get('teamBName', '')
    result = runPredictor(teamAId, teamAName, teamBId, teamBName)
    print result

if __name__ == '__main__':
    app.run(debug=True)