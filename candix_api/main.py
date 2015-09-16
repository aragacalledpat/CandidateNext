from flask import Flask, jsonify, request, abort, Response
import json
import logic

app = Flask(__name__)
@app.errorhandler(401)
def custom_401(error):
    return Response('valid token required', 401, {'WWWAuthenticate':'Basic realm="Login Required"'})

def valid_token(token):
    print token
    with open("tokens") as f:
        tokens = f.readlines()
        for element in tokens:
            element = element.strip("\n")
            if element == token:
                return True
            print token + " and " + element
        if token in tokens:
            print "returning true"
            return True
        else:
            print "returning false"
            return False

@app.route('/api/states')
def get_states():
    if "token" not in request.args or not valid_token(request.args.get("token")):
        abort(401)

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
    if "uservotes" in request.args:
        return jsonify(uservotes=logic.get_users_votes_on_bill(bill_id))
    elif "mostignored" in request.args:
        return jsonify(most_ignored_bills=logic.get_most_ignored_bills())
    else:
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

@app.route('/api/tags')
def get_most_followed_tags():
    return jsonify(most_followed=logic.most_folowed_tags())

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
