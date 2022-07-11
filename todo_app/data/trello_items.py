import requests
import os


def get_lists():
    url = "https://api.trello.com/1/boards/" + os.getenv('BOARD_ID') + "/lists"
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN'), 'cards': 'open'}

    response = (requests.get(url, params=query)).json()

    return response

def get_todo():
    todolist = (get_lists())[0]['cards']

    cards = []

    for card in todolist:
        item = {'id': card['id'], 'status': 'Not Started', 'title': card['name']}
        cards.append(item)

    return cards

