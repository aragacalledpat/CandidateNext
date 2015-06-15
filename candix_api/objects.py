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
