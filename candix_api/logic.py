import data_access
from collections import defaultdict

def get_candidates():
    candidate_tuples = data_access.get_candidates()

    #convert to list of dictionaries and make the values all uniocde
    candidates = []
    for candidate in candidate_tuples:
        candidate_dict = dict(candidate._asdict())

        for key in candidate_dict:
            candidate_dict[key] = unicode(candidate_dict[key], "utf-8", errors="replace")

        candidates.append(candidate_dict)

    return candidates

def get_candidate(candix_congress_id):
    candidate_tuple = data_access.get_candidate(candix_congress_id)
    return dict(candidate_tuple._asdict())

def recent_candidate_votes(candix_congress_id):
    congress_vote_tuples = data_access.recent_candidate_votes(candix_congress_id)
    congress_votes_dict = []

    for vote_tuple in congress_vote_tuples:
        vote_dict = dict(vote_tuple._asdict())
        congress_votes_dict.append(vote_dict)
    return congress_votes_dict

def get_bills(page_number):
    bill_tuples = data_access.get_bills(page_number)

    bills = []
    for bill in bill_tuples:
        bill_dict = dict(bill._asdict())
        bills.append(bill_dict)
    return bills

def get_bill(bill_id):
    bill_tuple = data_access.get_bill(bill_id)
    return dict(bill_tuple._asdict())

def get_top_bills():
    bills = data_access.get_top_hundred_bills()
    return bills

def get_states():
    return data_access.get_states()

def get_districts():
    district_tuples = data_access.get_districts()

    districts = defaultdict(list)
    for district_tuple in district_tuples:
        district_dict = dict(district_tuple._asdict())
        del district_dict["state"]
        del district_dict["candix_districts_id"]
        districts[district_tuple.state].append(district_dict)

    return dict(districts)

def get_district(dist_id):
    return data_access.get_district(dist_id)

def get_user_votes(user_id):
    return data_access.get_user_votes(user_id)

def get_bills_pagecount():
    return (data_access.get_bills_count() / 100) + 1
