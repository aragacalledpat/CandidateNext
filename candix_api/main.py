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


@app.route('/api/candidates/<candix_congress_id>')
def get_candidate(candix_congress_id):
    candidate = logic.get_candidate(candix_congress_id)
    return jsonify(candidate)

@app.route('/api/bills')
def get_bills():
    bill_list = logic.get_bills()
    return jsonify(bills=bill_list)

@app.route('/api/bills/<bill_id>')
def get_bill(bill_id):
    bill = logic.get_bill(bill_id)
    return jsonify(bill)

@app.route('/api/districts')
def get_districts():
    return jsonify(districts=logic.get_districts())

@app.route('/api/districts/<dist_id>')
def get_district(dist_id):
    return jsonify(users=logic.get_district(dist_id))

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
