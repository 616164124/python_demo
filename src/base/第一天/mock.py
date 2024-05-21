from unittest import mock

def userinfo(name):
    '''
    return: {'name':name}
    '''
    pass

def test_case():

    # mock userinfo
    userinfo = mock.Mock(return_value={'name': 'phyger'})

    # get result
    ret = userinfo('phyger')

    # judge
    if  ret == {'name': 'phyger'}:
        print('pass')
    else:
        print('not pass')

if __name__ == "__main__":
    test_case()