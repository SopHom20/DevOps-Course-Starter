import pytest
from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item

DEFAULT_ITEMS = [Item(1, 'List saved todo items', 'Not Started', '', None),
                 Item(1, 'Allow new items to be added', 'Not Started', '', None)]

DONE_ITEMS = [Item(3, 'TestOne', 'Completed', '', None), Item(4, 'TestTwo', 'Completed', '', None)]


@pytest.mark.parametrize("items, expected", [(DEFAULT_ITEMS, DEFAULT_ITEMS), (DONE_ITEMS, []),(DEFAULT_ITEMS + DONE_ITEMS, DEFAULT_ITEMS)])
def test_view_model_gets_not_started_items(items, expected):
    itemviewmodel = ViewModel(items)
    items = itemviewmodel.not_started_items
    assert items == expected


@pytest.mark.parametrize("items, expected",[(DEFAULT_ITEMS, []), (DONE_ITEMS, DONE_ITEMS), (DEFAULT_ITEMS + DONE_ITEMS, DONE_ITEMS)])
def test_view_model_gets_not_started_items(items, expected):
    itemviewmodel = ViewModel(items)
    items = itemviewmodel.completed_items
    assert items == expected
