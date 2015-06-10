import candix_api

#highest level modules exist
def test_modules_exist():
    assert('main' in dir(candix_api))
    assert('logic' in dir(candix_api))
    assert('data_access' in dir(candix_api))

def test_da_states_count():
    states = candix_api.data_access.get_states()
    assert(len(states) == 50)
