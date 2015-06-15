from flask import Flask, jsonify
import json
import logic

app = Flask(__name__)

@app.route('/api')
def hello_world():
    return 'Api Entry Point (add documentation here or something)!'

@app.route('/api/states')
def get_states():
    return jsonify(states=logic.get_states())


@app.route('/api/candidates')
def get_candidates():
    candis = logic.get_candidates()
    return jsonify(congresspeople=candis)


@app.route('/api/bills')
def get_bills():
    bills = logic.get_bills()
    return json.dumps(bills)


@app.route('/api/districts')
def get_districts():
    return jsonify(districts=logic.get_districts())

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
