from datetime import datetime

class Item:
    def __init__(self, id, title, status, desc, due):
        self._id = id
        self._title = title
        self._status = status
        self._desc = desc
        if due is None:
            self._due = "No due date"
        else:
            date = datetime.strptime(due[0:10], '%Y-%m-%d')
            self._due = "Due: " + date.strftime('%d/%m/%Y')

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def status(self):
        return self._status

    @property
    def desc(self):
        return self._desc

    @property
    def due(self):
        return self._due

    @id.setter
    def id(self, value):
        self._id = value

    @title.setter
    def title(self, value):
        self._title = value

    @status.setter
    def status(self, value):
        self._status = value

    @desc.setter
    def desc(self, value):
        self._desc = value

    @due.setter
    def due(self, value):
        self._due = value

    @classmethod
    def from_trello_card(cls, card, status):
        return cls(card['id'], card['name'], status, card['desc'], card['due'])
