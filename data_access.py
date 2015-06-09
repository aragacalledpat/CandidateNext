import MySQLdb
from ConfigParser import SafeConfigParser
from collections import defaultdict

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
    cur.execute("select post_id, meta_key, meta_value from nashxcix_cdx.wp_postmeta where post_id in\
                (SELECT post_id FROM nashxcix_cdx.wp_postmeta where meta_key='bioguide_id')\
                and meta_key = 'firstname' or meta_key = 'lastname' or meta_key = 'state'\
                or meta_key = 'party' order by post_id;")

    transformed_candidates = defaultdict(lambda : defaultdict(int))
    for row in cur.fetchall():
        cand_id = int(row[0])
        cand_prop = unicode(row[1], "utf-8")
        cand_prop_val = unicode(row[2], "utf-8", errors='replace')
        transformed_candidates[cand_id][cand_prop] = cand_prop_val

    for key,value in transformed_candidates.iteritems():
        transformed_candidates[key] = dict(value)

    return transformed_candidates

