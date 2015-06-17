import candix_api
import mock

#mocks for data access layer
def mock_get_candidates():
    return ()

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
