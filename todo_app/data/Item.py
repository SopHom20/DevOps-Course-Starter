class Item:
    def __init__(self, id, title, status, desc):
        self._id = id
        self._title = title
        self._status = status
        self._desc = desc
        self._editMode = False

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
    def editMode(self):
        return self._editMode

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

    @editMode.setter
    def editMode(self, value):
        self._editMode = value

    @classmethod
    def from_trello_card(cls, card, status):
        return cls(card['id'], card['name'], status, card['desc'])
