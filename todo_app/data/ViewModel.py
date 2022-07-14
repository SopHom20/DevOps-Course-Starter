class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def not_started_items(self):
        return self.filter_items(self.items, "Not Started")

    @property
    def completed_items(self):
        return self.filter_items(self.items, "Completed")

    @classmethod
    def filter_items(cls, items, status):
        return [item for item in items if item.status == status]