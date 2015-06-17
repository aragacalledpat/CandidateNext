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
    return ()

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

