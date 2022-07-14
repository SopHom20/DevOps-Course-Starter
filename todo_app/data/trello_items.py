import requests
import os
from todo_app.data.Item import Item


def build_parameters(extraparams={}):
    query = {'key': os.getenv('API_KEY'), 'token': os.getenv('TOKEN')}
    query.update(extraparams)
    return query


def build_url(endpoint=""):
    url = "https://api.trello.com/1/" + endpoint
    return url


def get_lists():
    board_id = os.getenv('BOARD_ID')
    url = build_url(f"boards/{board_id}/lists")
    query = build_parameters({'cards': 'open'})
    response = (requests.get(url, params=query)).json()

    return response


def alterCardInfo(list, status):
    cards = []
    for card in list:
        cards.append(Item.from_trello_card(card, status))
    return cards


def get_todo():
    todolist = (get_lists())[0]
    todocards = todolist['cards']
    return alterCardInfo(todocards, 'Not Started')


def get_done():
    donelist = (get_lists())[1]
    donecards = donelist['cards']
    return alterCardInfo(donecards, 'Completed')


def get_all_items():
    return get_todo() + get_done()


def create_card(title):
    todolist = (get_lists())[0]
    todolistid = todolist['id']
    url = build_url("cards/")
    query = build_parameters({'idList': todolistid, 'name': title})

    requests.post(url, params=query)


def delete_card(id):
    url = build_url("cards/" + id)
    query = build_parameters()
    requests.delete(url, params=query)


def update_card(id, query):
    url = build_url("cards/" + id)
    requests.put(url, params=query)


def complete_item(id):
    donelist = (get_lists())[1]
    donelistid = donelist['id']
    update_card(id, build_parameters({'idList': donelistid}))


def undo_complete(id):
    todolist = (get_lists())[0]
    todolistid = todolist['id']
    update_card(id, build_parameters({'idList': todolistid}))


def edit_desc(id, desc):
    update_card(id, build_parameters({'desc': desc}))


def edit_due_date(id, date):
    update_card(id, build_parameters({'due': date}))
