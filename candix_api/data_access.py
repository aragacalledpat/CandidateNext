import MySQLdb
from ConfigParser import SafeConfigParser
from collections import defaultdict
import objects

def get_db_connection():
    parser = SafeConfigParser()
    parser.read('db_connection')
    config_host = parser.get('connection', 'host')
    config_user = parser.get('connection','user')
    config_password = parser.get('connection', 'passwd')
    config_db = parser.get('connection', 'db')
    return MySQLdb.connect(host=config_host,
                            user=config_user,
                            passwd=config_password,
                            db=config_db)


def get_candidates():
    #returns all candidates but only firstname, lastname, party and state
    #this will get rewritten once the tables get fixed
    db_conn = get_db_connection()
    cur = db_conn.cursor()
    cur.execute("select candix_congress_id, firstname, lastname, gender, party, state, district from candix_congress")
    congress_tuples = map(objects.Short_CongressPersonRecord._make, cur.fetchall())

    candidates = {}
    for congressperson in congress_tuples:

        #add record to dictionary using ID as the key
        candix_id = int(congressperson.ID)
        congress_dict = dict(congressperson._asdict())
        del congress_dict["ID"]

        #make sure we have the right encoding
        for key in congress_dict:
            congress_dict[key] = unicode(congress_dict[key], "utf-8", errors="replace")

        candidates[candix_id] = congress_dict

    return candidates

def get_bill_ids():
    db_conn = get_db_connection()
    cur = db_conn.cursor()
    cur.execute("select distinct post from wp_voteiu_data where not vote = 1 order by post")
    bill_ids = []
    for item in cur.fetchall():
        bill_ids.append(int(item[0]))
    return bill_ids

def get_bill_from_id(bill_id):
    db_conn = get_db_connection()
    cur = db_conn.cursor()
    cur.execute("select meta_key, meta_value from wp_postmeta where post_id=" + str(bill_id))
    bill_details = []

    for detail in cur.fetchall():
        bill_details.append(detail)
    return bill_details

def get_states():
    return ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
            "DE", "FL", "GA", "HI", "ID", "IL", "IN",
            "IA", "KS", "KY", "LA", "ME", "MD", "MA",
            "MI", "MN", "MS", "MO", "MT", "NE", "NV",
            "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
            "OK", "OR", "PA", "RI", "SC", "SD", "TN",
            "TX", "UT", "VT", "VA", "WA", "WV", "WI",
            "WY"]


