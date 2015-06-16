import data_access
from collections import defaultdict

def get_candidates():
    return data_access.get_candidates()

def get_bills():
    return data_access.get_bills()

def get_states():
    return data_access.get_states()

def get_districts():
    return data_access.get_districts()

def get_district(dist_id):
    return data_access.get_district(dist_id)
