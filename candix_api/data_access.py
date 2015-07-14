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

def do_mysql(sql_action):
    db_conn = get_db_connection()
    cur = db_conn.cursor()
    cur.execute(sql_action)
    db_conn.close()
    return cur.fetchall()

def get_candidates():
    result = do_mysql("select candix_congress_id, firstname, lastname, gender, party, state, district from candix_congress")
    congress_tuples = map(objects.Short_CongressPersonRecord._make, result)

    #convert "ID" which comes back as a long to be a string
    for i, congress_tuple in enumerate(congress_tuples):
        congress_id = str(int(congress_tuple.ID))
        congress_tuple = congress_tuple._replace(ID=congress_id)
        congress_tuples[i] = congress_tuple

    return congress_tuples

def get_candidate(candix_congress_id):
    result = do_mysql("select * from candix_congress where candix_congress_id = " + candix_congress_id)
    first_row = result[0]
    candidate_tuple = objects.CongressPersonRecord._make(first_row)

    #reformat datetimes to be strings
    formatted_bday = candidate_tuple.birthdate.strftime("%Y-%m-%d")
    candidate_tuple = candidate_tuple._replace(birthdate=formatted_bday)
    return candidate_tuple

def get_bills_count():
    result = do_mysql("select count(*)  from candix_bills")
    return result[0][0]

def get_bills(page_count):
    start_at = (int(page_count) - 1) * 100
    result = do_mysql("select bill_id, chamber, introduced_on, official_title, last_action_at from candix_bills order by introduced_on DESC LIMIT " + str(start_at) + ", 100")
    bills_tuples = map(objects.Short_Bill._make, result)

    for i, bill in enumerate(bills_tuples):
        last_action_date = bill.last_action_at.strftime('%Y-%m-%d')
        bill = bill._replace(last_action_at=last_action_date)
        bills_tuples[i] = bill

    return bills_tuples


def get_bill(bill_id):
    result = do_mysql("select * from candix_bills where bill_id = \"" + bill_id + "\"")
    first_row = result[0]
    bill_tuple = objects.Bill._make(first_row)

    last_action = bill_tuple.last_action_at.strftime('%Y-%m-%d')
    last_version = bill_tuple.last_version_on.strftime('%Y-%m-%d')
    bill_tuple = bill_tuple._replace(last_action_at=last_action, last_version_on=last_version)

    return bill_tuple

def recent_candidate_votes(candix_congress_id):
    result = do_mysql("SELECT candix_votes_congress.type, candix_bills.bill_id,candix_votes_congress.timestamp FROM candix_votes_congress "
            "LEFT JOIN candix_congress on candix_votes_congress.vote = candix_congress.bioguide_id "
            "LEFT JOIN candix_bills on candix_votes_congress.post = candix_bills.wp_post_id "
            "WHERE candix_congress_id = " + str(candix_congress_id)  + " AND candix_bills.bill_id is not null "
            "order by candix_votes_congress.timestamp desc LIMIT 100")

    congress_votes_tuples = map(objects.Congress_Vote._make, result)

    for i, congress_vote_tuple in enumerate(congress_votes_tuples):
        vote_date = str(congress_vote_tuple.timestamp)
        readable_vote = congress_vote_tuple.vote
        if readable_vote == "vote":
            readable_vote = "yea"
        if readable_vote == "sink":
            readable_vote = "nay"
        congress_vote_tuple = congress_vote_tuple._replace(timestamp=vote_date,vote=readable_vote)
        congress_votes_tuples[i] = congress_vote_tuple

    return congress_votes_tuples

def get_states():
    return ["AL", "AK", "AZ", "AR", "CA", "CO", "CT",
            "DE", "FL", "GA", "HI", "ID", "IL", "IN",
            "IA", "KS", "KY", "LA", "ME", "MD", "MA",
            "MI", "MN", "MS", "MO", "MT", "NE", "NV",
            "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
            "OK", "OR", "PA", "RI", "SC", "SD", "TN",
            "TX", "UT", "VT", "VA", "WA", "WV", "WI",
            "WY"]

def get_districts():
    result = do_mysql("select * from candix_districts")
    district_tuples = map(objects.District._make, result)

    for i, district_tuple in enumerate(district_tuples):
        dist_id = int(district_tuple.district)
        candix_dist_id = int(district_tuple.candix_districts_id)
        district_tuple = district_tuple._replace(district=dist_id,candix_districts_id=candix_dist_id)
        district_tuples[i] = district_tuple

    return district_tuples


def get_district(dist_id):
    result = do_mysql("SELECT user_id FROM nashxcix_cdx.wp_usermeta where meta_key=\"district\" and meta_value = "+ dist_id  + ";")
    userIds = []
    for user in result:
        userIds.append(user[0])

    return userIds

def get_user_votes(user_id):
    result = do_mysql("SELECT candix_votes_users_bills.type, "
            "candix_bills.bill_id, candix_votes_users_bills.timestamp from candix_votes_users_bills "
            "inner join candix_bills on candix_bills.wp_post_id = candix_votes_users_bills.post where vote=" + user_id)

    user_votes = map(objects.User_Votes._make, result)
    for i, opinion in enumerate(user_votes):
        if opinion.vote == "vote":
          user_votes[i] = opinion._replace(vote="yea")

    return user_votes

def get_top_hundred_bills():
    result = do_mysql("select candix_bills.bill_id from candix_bills "
            "left join wp_postmeta "
            "on candix_bills.wp_post_id= wp_postmeta.post_id "
            "where wp_postmeta.meta_key=\"voteiu\" "
            "order by meta_value desc limit 100")
    bill_ids = []
    for thing in result:
        bill_ids.append(thing[0])
    return bill_ids
