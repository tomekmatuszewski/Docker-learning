import requests
import random

base_uri = 'http://localhost'
port = 3000
posts_uri = f'{base_uri}:{port}/posts'


def test_api_get_posts():
	r = requests.get(posts_uri)
	assert r.status_code == 200

def test_creating_post():
	marker = random.randint(1, 100000)
	body = {'title': 'test post', 'author': 'ag'}
	r = requests.post(posts_uri, json=body)
	assert r.status_code == 201