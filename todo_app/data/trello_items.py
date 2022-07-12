import requests
import os
from todo_app.data.Item import Item

def get_lists():
    url = "https://api.trello.com/1/boards/" + os.getenv('BOARD_ID') + "/lists"
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN'), 'cards': 'open'}

    response = (requests.get(url, params=query)).json()

    return response


def alterCardInfo(list, status):
    cards = []
    for card in list:
        cards.append(Item.from_trello_card(card, status))
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

def delete_card(item):
    url = "https://api.trello.com/1/cards/" + item
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN')}
    requests.delete(url, params=query)

def move_item(item, listid):
    url = "https://api.trello.com/1/cards/" + item
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN'), 'idList': listid}
    requests.put(url, params=query)

def complete_item(item):
    move_item(item, (get_lists())[1]['id'] )

def undo_complete(item):
    move_item(item, (get_lists())[0]['id'] )

def edit_item(item, desc):
    url = "https://api.trello.com/1/cards/" + item
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN'), 'desc': desc}
    requests.put(url, params=query)