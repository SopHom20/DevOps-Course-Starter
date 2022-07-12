class Item:
    def __init__(self, id, title, status):
        self._id = id
        self._title = title
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def status(self):
        return self._status

    @id.setter
    def id(self, value):
        self._id = value

    @title.setter
    def title(self, value):
        self._title = value

    @status.setter
    def status(self, value):
        self._status = value

    @classmethod
    def from_trello_card(cls, card, status):
        return cls(card['id'], card['name'], status)
