from collections import namedtuple

CongressPersonRecord = namedtuple('CongressPersonRecord', ['candix_congress_id', "candix_districts_path_id",
                                                            'wp_post_id', 'bioguide_id', 'birthdate',
                                                            'congresspedia_url', 'congress_office', 'crp_id',
                                                            'district','facebook_id', 'fax', 'fec_id', 'firstname',
                                                            'gender', 'govtrack_id', 'in_office', 'lastname', 'middlename',
                                                            'name_suffix', 'nickname', 'oc_email', 'official_rss', 'party',
                                                            'phone', 'senate_class', 'state', 'title', 'twitter_id', 'voteiu',
                                                            'votesmart_id', 'webform', 'website', 'youtube_url'])

Short_CongressPersonRecord = namedtuple('Short_CongressPersonRecord', ['ID', 'firstname', 'lastname', 'gender', 'party', 'state', 'district'])

District = namedtuple('District', ['candix_districts_id', 'candix_districts_path_id','state' ,'district'])

Bill = namedtuple('Bill', ['candix_bill_id', 'wp_post_id', 'bill_id', 'bill_type',
                            'chamber', 'committee_ids', 'congress','cosponsors_count',
                            'cosponsor_ids', 'enacted_as', 'history', 'introduced_on',
                            'keywords', 'last_action', 'last_action_at', 'last_version',
                            'last_version_on', 'last_vote_at', 'number', 'official_title',
                            'popular_title', 'related_bill_ids', 'search', 'short_title',
                            'sponsor', 'sponsor_id', 'summary', 'summary_short', 'titles',
                            'voteiu', 'not_interested','withdrawn_cosponsors_count'])

Short_Bill = namedtuple('Short_Bill', ['bill_id', 'chamber', 'introduced_on', 'official_title','last_action_at'])

User_Votes = namedtuple('User_Votes', ['vote', 'bill_id', 'timestamp'])

