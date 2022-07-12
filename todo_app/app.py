from operator import attrgetter, itemgetter

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from todo_app.data.ViewModel import ViewModel
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_all_items, create_card, delete_card, complete_item, undo_complete, edit_desc, edit_due_date

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = sorted(get_all_items(), key=lambda i: i.status, reverse=True)
    item_view_model = ViewModel(items)
    return render_template('index.html', view_model=item_view_model)


@app.route('/add', methods=['POST'])
def addItem():
    tasktitle = request.form.get('title')
    create_card(tasktitle)
    return redirect(url_for('index'))


@app.route('/complete', methods=['POST'])
def completeItem():
    id = request.form['completeBtn']
    complete_item(id)
    return redirect(url_for('index'))


@app.route('/undocomplete', methods=['POST'])
def undoCompleteItem():
    id = request.form['uncompleteBtn']
    undo_complete(id)
    return redirect(url_for('index'))


@app.route('/remove', methods=['POST'])
def removeItem():
    id = request.form['removeBtn']
    delete_card(id)
    return redirect(url_for('index'))


@app.route('/editDesc', methods=['POST'])
def editItemDesc():
    id = request.form['updateDescBtn']
    newdesc = request.form.get('desc')
    edit_desc(id, newdesc)
    return redirect(url_for('index'))


@app.route('/editDueDate', methods=['POST'])
def editItemDueDate():
    date = request.form.get('date')
    if date != "":
        date = datetime.strptime(date, '%d/%m/%Y')
    edit_due_date(request.form['updateDateBtn'], date)
    return redirect(url_for('index'))
