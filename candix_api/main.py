from flask import Flask, jsonify, request
import json
import logic

app = Flask(__name__)


@app.route('/api/states')
def get_states():
    return jsonify(states=logic.get_states())


@app.route('/api/candidates')
def get_candidates():
    candis = logic.get_candidates()
    return jsonify(congresspeople=candis)


@app.route('/api/candidates/<candix_congress_id>')
def get_candidate(candix_congress_id):
    if "recent" in request.args:
        recent_votes = logic.recent_candidate_votes(candix_congress_id)
        return jsonify(recentVotes=recent_votes)
    else:
        candidate = logic.get_candidate(candix_congress_id)
        return jsonify(candidate)

@app.route('/api/bills')
def get_bills():
    if "page" in request.args:
        bill_list = logic.get_bills(request.args.get('page'))
        return jsonify(bills=bill_list)
    else:
        return jsonify(pageCount=logic.get_bills_pagecount())

@app.route('/api/bills/<bill_id>')
def get_bill(bill_id):
    bill = logic.get_bill(bill_id)
    return jsonify(bill)

@app.route('/api/bills/trending')
def get_top_bills():
    bills = logic.get_top_bills()
    return jsonify(trending=bills)

@app.route('/api/districts')
def get_districts():
    return jsonify(districts=logic.get_districts())

@app.route('/api/districts/<dist_id>')
def get_district(dist_id):
    return jsonify(users=logic.get_district(dist_id))

@app.route('/api/users/<user_id>')
def get_user_votes(user_id):
    return jsonify(votes=logic.get_user_votes(user_id))


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
