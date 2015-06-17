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

def get_bills():
    return data_access.get_bills()

def get_bill(bill_id):
    return data_access.get_bill(bill_id)

def get_states():
    return data_access.get_states()

def get_districts():
    return data_access.get_districts()

def get_district(dist_id):
    return data_access.get_district(dist_id)
