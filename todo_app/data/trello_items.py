import requests
import os


def get_lists():
    url = "https://api.trello.com/1/boards/" + os.getenv('BOARD_ID') + "/lists"
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN'), 'cards': 'open'}

    response = (requests.get(url, params=query)).json()

    return response


def alterCardInfo(list, status):
    cards = []
    for card in list:
        item = {'id': card['id'], 'status': status, 'title': card['name']}
        cards.append(item)
    return cards


def get_todo():
    todolist = (get_lists())[0]['cards']

    return alterCardInfo(todolist, 'Not Started')


def get_done():
    todolist = (get_lists())[1]['cards']
    return alterCardInfo(todolist, 'Completed')


def get_all_items():
    return get_todo() + get_done()

def create_card(title):
    listid = (get_lists())[0]['id']
    url = "https://api.trello.com/1/cards/"
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN'), 'name': title, 'idList': listid}

    requests.post(url, params=query)