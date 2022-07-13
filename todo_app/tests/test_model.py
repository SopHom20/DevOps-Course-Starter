import pytest
from todo_app.data.ViewModel import ViewModel

DEFAULT_ITEMS = [
    {'id': 1, 'status': 'Not Started', 'title': 'List saved todo items'},
    {'id': 2, 'status': 'Not Started', 'title': 'Allow new items to be added'}
]

DONE_ITEMS = [
    {'id': 3, 'status': 'Completed', 'title': 'TestOne'},
    {'id': 4, 'status': 'Completed', 'title': 'TestTwo'}
]


@pytest.mark.parametrize("items, expected", [(DEFAULT_ITEMS, DEFAULT_ITEMS), (DONE_ITEMS, []), (DEFAULT_ITEMS + DONE_ITEMS, DEFAULT_ITEMS)])
def test_view_model_gets_not_started_items(items, expected):
    itemviewmodel = ViewModel(items)
    items = itemviewmodel.not_started_items
    assert items == expected

@pytest.mark.parametrize("items, expected", [(DEFAULT_ITEMS, []), (DONE_ITEMS, DONE_ITEMS), (DEFAULT_ITEMS + DONE_ITEMS, DONE_ITEMS)])
def test_view_model_gets_not_started_items(items, expected):
    itemviewmodel = ViewModel(items)
    items = itemviewmodel.completed_items
    assert items == expected