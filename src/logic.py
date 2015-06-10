import data_access
from collections import defaultdict

def get_candidates():
    return data_access.get_candidates()

def get_bills():
    bills = defaultdict(lambda: defaultdict(str))
    bill_ids = data_access.get_bill_ids()

    for bill_id in bill_ids:
        bill_details = data_access.get_bill_from_id(bill_id)
        for detail in bill_details:
            bills[bill_id][detail[0]] = detail[1]
    return bills


def get_states():
    return ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
            "DE", "FL", "GA", "HI", "ID", "IL", "IN",
            "IA", "KS", "KY", "LA", "ME", "MD", "MA",
            "MI", "MN", "MS", "MO", "MT", "NE", "NV",
            "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
            "OK", "OR", "PA", "RI", "SC", "SD", "TN",
            "TX", "UT", "VT", "VA", "WA", "WV", "WI",
            "WY"]
