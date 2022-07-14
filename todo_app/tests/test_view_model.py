import pytest
from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item

default_items = [Item(1, 'List saved todo items', 'Not Started', '', None),
                 Item(1, 'Allow new items to be added', 'Not Started', '', None)]

done_items = [Item(3, 'TestOne', 'Completed', '', None), Item(4, 'TestTwo', 'Completed', '', None)]


@pytest.mark.parametrize("items, expected", [(default_items, default_items), (done_items, []), (default_items + done_items, default_items)])
def test_view_model_gets_not_started_items(not_started_items, expected):
    item_view_model = ViewModel(not_started_items)
    not_started_items = item_view_model.not_started_items
    assert not_started_items == expected


@pytest.mark.parametrize("items, expected", [(default_items, []), (done_items, done_items), (default_items + done_items, done_items)])
def test_view_model_gets_not_started_items(completed_items, expected):
    item_view_model = ViewModel(completed_items)
    completed_items = item_view_model.completed_items
    assert completed_items == expected