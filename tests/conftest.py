import pytest
import requests

@pytest.fixture
def base():
    return 'https://zmyslonyadres.com'

class Todos:
    def __init__(self, base):
        self.base = base


    def register(self, name, gmail, password):
        return requests.post(f'{self.base}/register', json={'username': name, 'gmail': gmail, 'password': password})

    def login(self, name, gmail, password):
        return requests.post(f'{self.base}/login', json={'username': name, 'gmail': gmail, 'password': password})
    

    def add_post(self, content, header):
        return requests.post(f'{self.base}/posts', json={'content': content}, headers=header)
    
    def get_post_by_id(self, id, header):
        return requests.get(f'{self.base}/posts/{id}', headers=header)
    
    def get_all_posts(self, header):
        return requests.get(f'{self.base}/posts/', headers=header)
    

