import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import os
import requests


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = app.create_app()

    with test_app.test_client() as client:
        yield client


class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data


# Stub replacement for requests.get(url)
def stub(url, params={}):
    test_board_id = os.environ.get('BOARD_ID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists':
        fake_response_data = [{
            'id': '1',
            'name': 'To Do',
            'cards': [{'id': '123', 'name': 'Test1', 'desc': '', 'due': None}]
        }, {
            'id': '2',
            'name': 'Done',
            'cards': [{'id': '456', 'name': 'Test2', 'desc': '', 'due': None}]
        }]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')


def test_index_page(monkeypatch, client):
    # Replace requests.get(url) with our own function
    monkeypatch.setattr(requests, 'get', stub)

    # Make a request to our app's index page
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test1' in response.data.decode()
    assert 'Test2' in response.data.decode()
