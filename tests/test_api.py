import candix_api
from candix_api import data_access, logic, objects, main
import mock

#mocks for data access layer
def mock_get_candidates():
    mock_candidates = []
    mock_candidates.append(objects.Short_CongressPersonRecord("3581", "Neil", "Abercrombie", "M", "D", "HI","1"))
    mock_candidates.append(objects.Short_CongressPersonRecord("4098", "Barry", "Loudermilk", "M", "R", "GA", "11"))
    return mock_candidates

def mock_get_candidate(candix_congress_id):
    return objects.CongressPersonRecord(3581L, 'HI-1', 2796L, 'A000014', '1938-06-26', 'http://www.opencongress.org/wiki/Neil_Abercrombie', '', 'N00007665', '1', '', '', 'H6HI01121', 'Neil', 'M', '400001', 0, 'Abercrombie', '', '', '', '', '', 'D', '', '', 'HI', 'Rep', 'neilabercrombie', None, '26827', '', 'http://www.house.gov/abercrombie', 'http://youtube.com/hawaiirep1')


def mock_get_bills():
    return ()

def mock_get_bill(bill_id):
    return ()

def mock_get_districts():
    return ()

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

