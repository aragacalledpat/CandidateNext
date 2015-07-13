import candix_api
from candix_api import data_access, logic, objects, main
import mock
import json

#mocks for data access layer
def mock_get_candidates():
    mock_candidates = []
    mock_candidates.append(objects.Short_CongressPersonRecord("3581", "Neil", "Abercrombie", "M", "D", "HI","1"))
    mock_candidates.append(objects.Short_CongressPersonRecord("4098", "Barry", "Loudermilk", "M", "R", "GA", "11"))
    return mock_candidates

def mock_get_candidate(candix_congress_id):
    return objects.CongressPersonRecord(3581L, 'HI-1', 2796L, 'A000014', '1938-06-26', 'http://www.opencongress.org/wiki/Neil_Abercrombie', '', 'N00007665', '1', '', '', 'H6HI01121', 'Neil', 'M', '400001', 0, 'Abercrombie', '', '', '', '', '', 'D', '', '', 'HI', 'Rep', 'neilabercrombie', None, '26827', '', 'http://www.house.gov/abercrombie', 'http://youtube.com/hawaiirep1')


def mock_get_bills(page_number):
    mock_bills = []
    mock_bills.append(objects.Short_Bill("hr2505-114", "house", "2015-05-21", "To amend title XVIII of the Social Security Act to require the annual reporting of data on enrollment in Medicare Advantage plans.", "2015-06-12"))
    mock_bills.append(objects.Short_Bill("hr1314-114", "house", "2015-06-10", "Providing for consideration of the Senate amendment to the bill (H.R. 1314) to amend the Internal Revenue Code of 1986 to provide for a right to an administrative appeal relating to adverse determinations of tax-exempt status of certain organizations, and", "2015-06-11"))
    return mock_bills

def mock_get_bill(bill_id):
    return objects.Bill(7L, 18199L, 'hres305-114', 'hres', 'house', 'a:1:{i:0;s:4:"HSRU";}', '114', 0L, 'a:0:{}', '', 'a:5:{s:18:"awaiting_signature";b:0;s:7:"enacted";b:0;s:6:"vetoed";b:0;s:6:"active";b:1;s:9:"active_at";s:20:"2015-06-11T06:02:00Z";}', '2015-06-10', 'a:0:{}', 'a:7:{s:8:"calendar";s:5:"House";s:6:"number";s:2:"40";s:10:"references";a:0:{}s:8:"acted_at";s:20:"2015-06-11T06:02:00Z";s:4:"text";s:46:"Placed on the House Calendar, Calendar No. 40.";s:4:"type";s:8:"calendar";s:5:"under";N;}', '2015-06-11', None, '2015-06-10', None, 305L, 'Providing for consideration of the Senate amendment to the bill (H.R. 1314) to amend the Internal Revenue Code of 1986 to provide for a right to an administrative appeal relating to adverse determinations of tax-exempt status of certain organizations, and', '', 'a:2:{i:0;s:9:"hr644-114";i:1;s:10:"hr1314-114";}', 'a:2:{s:5:"score";i:1;s:4:"type";s:4:"bill";}', '', 'a:33:{s:8:"birthday";s:10:"1955-03-22";s:11:"bioguide_id";s:7:"S000250";s:6:"gender";s:1:"M";s:7:"fec_ids";a:1:{i:0;s:9:"H2TX03126";}s:6:"office";s:34:"2233 Rayburn House Office Building";s:5:"title";s:3:"Rep";s:6:"crp_id";s:9:"N00005681";s:7:"chamber";s:', 'Sets forth the rule for consideration of the Senate amendment to the bill (H.R. 1314) to amend the Internal Revenue Code of 1986 to provide for a right to an administrative appeal relating to adverse determinations of tax-exempt status of certain organizations, and providing for consideration of the Senate amendments to the bill (H.R. 644) to amend the Internal Revenue Code of 1986 to permanently extend and expand the charitable deduction for contributions of food inventory.', 'Sets forth the rule for consideration of the Senate amendment to the bill (H.R. 1314) to amend the Internal Revenue Code of 1986 to provide for a right to an administrative appeal relating to adverse determinations of tax-exempt status of certain organizations, and providing for consideration of the Senate amendments to the bill (H.R. 644) to amend the Internal Revenue Code of 1986 to permanently extend and expand the charitable deduction for contributions of food inventory.', 'a:1:{i:0;a:4:{s:2:"as";s:10:"introduced";s:14:"is_for_portion";b:0;s:5:"title";s:469:"Providing for consideration of the Senate amendment to the bill (H.R. 1314) to amend the Internal Revenue Code of 1986 to provide for a right to an administrative appeal relating to adverse determinations of tax-exempt status of certain organizations, and providing for consideration of the Senate amendments to the bill (H.R. 644) to amend the Internal Revenue Code of 1986 to permanently extend and expand the charitable deduction for contributions of food inventory.";s:4:"type";s:8:"official";}}', 0L, 0L, '0')

def mock_get_districts():
    mock_districts = []
    mock_districts.append(objects.District(3648, "AK-0", "AK", 4))
    mock_districts.append(objects.District(3358, "CA-31", "CA", 31))
    mock_districts.append(objects.District(2949, "CA-34", "CA", 34))
    return mock_districts

#highest level modules exist
def test_modules_exist():
    assert('main' in dir(candix_api))
    assert('logic' in dir(candix_api))
    assert('data_access' in dir(candix_api))

def test_states_count():
    states = candix_api.data_access.get_states()
    assert(len(states) == 50)

@mock.patch('candix_api.data_access.get_candidates', side_effect=mock_get_candidates)
def test_lg_getcandidates_returnslist(mocked_function):
    candidates = logic.get_candidates()
    assert isinstance(candidates,list)



@mock.patch('candix_api.data_access.get_candidates', side_effect=mock_get_candidates)
def test_lg_getcandidates_returnhasdicts(mocked_function):
    candidates = logic.get_candidates()
    for candidate in candidates:
        assert isinstance(candidate, dict)


@mock.patch('candix_api.data_access.get_candidates', side_effect=mock_get_candidates)
def test_lg_getcandidates_hasallfields(mocked_function):
    candidates = logic.get_candidates()
    assert len(candidates[0].keys()) == 7
    assert 'ID' in candidates[0]
    assert 'firstname' in candidates[0]
    assert 'state' in candidates[0]


@mock.patch('candix_api.data_access.get_candidate', side_effect=mock_get_candidate)
def test_lg_getcandidate_returns_dict(mocked_function):
    candidate= logic.get_candidate('3581')
    assert isinstance(candidate,dict)


@mock.patch('candix_api.data_access.get_candidate', side_effect=mock_get_candidate)
def test_lg_getcandidate_hasfields(mocked_function):
    candidate= logic.get_candidate('3581')
    assert len(candidate.keys()) == 33
    assert 'birthdate' in candidate
    assert 'website' in candidate
    assert 'district' in candidate
    assert 'candix_congress_id' in candidate
    assert 'in_office' in candidate
    assert 'firstname' in candidate
    assert 'phone' in candidate


@mock.patch('candix_api.data_access.get_bills', side_effect=mock_get_bills)
def test_lg_getbills_returns_list(mocked_function):
    bills = logic.get_bills(1)
    assert isinstance(bills, list)


@mock.patch('candix_api.data_access.get_bills', side_effect=mock_get_bills)
def test_lg_getbills_returns_containsdicts(mocked_function):
    bills = logic.get_bills(1)
    for bill in bills:
        assert isinstance(bill, dict)

@mock.patch('candix_api.data_access.get_bills', side_effect=mock_get_bills)
def test_lg_getbills_return_hasfields(mocked_function):
    bills = logic.get_bills(1)
    assert len(bills[0].keys()) == 5
    assert 'official_title' in bills[0]
    assert 'last_action_at' in bills[0]


@mock.patch('candix_api.data_access.get_bill', side_effect=mock_get_bill)
def test_lg_getbill_return_isdict(mocked_function):
    bill = logic.get_bill(42)
    assert isinstance(bill,dict)


@mock.patch('candix_api.data_access.get_bill', side_effect=mock_get_bill)
def test_lg_getbill_return_hasfields(mocked_function):
    bill = logic.get_bill(42)
    assert len(bill.keys()) == 31
    assert 'candix_bill_id' in bill
    assert 'last_version' in bill
    assert 'bill_type' in bill
    assert 'last_action' in bill
    assert 'short_title' in bill


@mock.patch('candix_api.data_access.get_districts', side_effect=mock_get_districts)
def test_lg_getdistricts_returnisdict(mocked_function):
    districts = logic.get_districts()
    assert isinstance(districts,dict)


@mock.patch('candix_api.data_access.get_districts', side_effect=mock_get_districts)
def test_lg_getdistricts_keysarestates(mocked_function):
    districts = logic.get_districts()
    states = logic.get_states()
    for key in districts.keys():
        assert key in states


@mock.patch('candix_api.data_access.get_districts', side_effect=mock_get_districts)
def test_lg_getdistricts_valuesarelists(mocked_function):
    districts = logic.get_districts()
    assert isinstance(districts["CA"], list)


@mock.patch('candix_api.data_access.get_districts', side_effect=mock_get_districts)
def test_lg_getdistricts_listitemsaredicts(mocked_function):
    districts = logic.get_districts()
    assert isinstance(districts["CA"][0], dict)


@mock.patch('candix_api.data_access.get_districts', side_effect=mock_get_districts)
def test_lg_getdistricts_districts_havecorrectfields(mocked_function):
    districts = logic.get_districts()
    first_cali_district = districts["CA"][0]
    assert len(first_cali_district.keys()) == 2
    assert 'state' not in first_cali_district
    assert 'candix_districts_id' not in first_cali_district
    assert 'candix_districts_path_id' in first_cali_district
    assert 'district' in first_cali_district

def test_main_getstates_returnsjson():
    with main.app.test_client() as c:
        rv = c.get('/api/states')
        json.loads(rv.data)


@mock.patch('candix_api.data_access.get_candidates', side_effect=mock_get_candidates)
def test_main_getcandidates_returnsjson(mocked_function):
    with main.app.test_client() as c:
        rv = c.get('/api/candidates')
        json.loads(rv.data)


@mock.patch('candix_api.data_access.get_candidate', side_effect=mock_get_candidate)
def test_main_getcandidate_returnsjson(mocked_function):
    with main.app.test_client() as c:
        rv = c.get('/api/candidates/3581')
        json.loads(rv.data)

@mock.patch('candix_api.data_access.get_bill', side_effect=mock_get_bill)
def test_main_bill_returnsjson(mocked_function):
    with main.app.test_client() as c:
        rv = c.get('/api/bills/hr2505-114')
        json.loads(rv.data)


@mock.patch('candix_api.data_access.get_districts', side_effect=mock_get_districts)
def test_main_districts_returnsjson(mocked_function):
    with main.app.test_client() as c:
        rv = c.get('/api/districts')
        json.loads(rv.data)
