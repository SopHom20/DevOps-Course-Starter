import os
import pytest
from threading import Thread
from time import sleep
from dotenv import load_dotenv
from todo_app import app
import requests

from selenium import webdriver


@pytest.fixture(scope='module')
def app_with_temp_board():
    # Load our real environment variables
    load_dotenv(override=True)

    # Create the new board & update the board id environment variable
    board_id = create_trello_board()
    os.environ['BOARD_ID'] = board_id

    # Construct the new application
    application = app.create_app()

    # Start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()

    # Give the app a moment to start
    sleep(1)

    # Return the application object as the result of the fixture
    yield application

    # Tear down
    thread.join(1)
    delete_trello_board(board_id)


def create_trello_board():
    url = "https://api.trello.com/1/boards"
    query = {'name': "Test Board", 'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN'),
             'idOrganization': os.getenv('ID_ORGANIZATION')}
    return requests.post(url, params=query).json()['id']


def delete_trello_board(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}"
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN')}
    requests.delete(url, params=query)


@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver


def test_task_journey(driver, app_with_temp_board):
    driver.get('http://localhost:5000/')

    assert driver.title == 'To-Do App'
