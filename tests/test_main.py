from conftest import Todos, base
import pytest

@pytest.fixture
def clt(base):
    Todos(base)


def header(clt):
    try:
        reg = clt.register('maciek', 'maciek@gmail.com', 'maciek1234')
    except:
        r = reg.status_code
        if r == 400:
            pass

    log = clt.login('maciek', 'maciek@gmail.com', 'maciek1234')

    tok = log.json()['token']

    heade = {'Authorization': f'Bearer {tok}'}

    return heade


def test_add_posts(clt, header):
    add = clt.add_post('Post', header)
    pj = add.json()

    pid = pj['id']

    gpi = clt.get_post_by_id(pid, header)

    assert gpi == {'content': 'Post'}

def test_all_posts(clt, header):
    get = clt.get_all_posts(header)
    getjson = get.json()

    assert any('content' in g for g in getjson)



