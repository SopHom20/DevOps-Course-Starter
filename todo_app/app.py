from operator import attrgetter, itemgetter

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from todo_app.flask_config import Config
from todo_app.data.trello_items import get_all_items, create_card, delete_card, complete_item, undo_complete, edit_desc, edit_due_date

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = sorted(get_all_items(), key=lambda i: i.status, reverse=True)
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def addItem():
    create_card(request.form.get('title'))
    return redirect(url_for('index'))


@app.route('/complete', methods=['POST'])
def completeItem():
    complete_item(request.form['completeBtn'])
    return redirect(url_for('index'))


@app.route('/undocomplete', methods=['POST'])
def undoCompleteItem():
    undo_complete(request.form['uncompleteBtn'])
    return redirect(url_for('index'))


@app.route('/remove', methods=['POST'])
def removeItem():
    delete_card(request.form['removeBtn'])
    return redirect(url_for('index'))


@app.route('/editDesc', methods=['POST'])
def editItemDesc():
    edit_desc(request.form['updateDescBtn'], request.form.get('desc'))
    return redirect(url_for('index'))


@app.route('/editDueDate', methods=['POST'])
def editItemDueDate():
    date = request.form.get('date')
    if date != "":
        date = datetime.strptime(date, '%d/%m/%Y')
    edit_due_date(request.form['updateDateBtn'], date)
    return redirect(url_for('index'))
