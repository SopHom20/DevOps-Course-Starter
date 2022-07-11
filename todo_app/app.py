from operator import attrgetter, itemgetter

from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, get_item, save_item, remove_item
from todo_app.data.trello_items import get_todo

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = sorted(get_todo(), key=lambda i: i['status'], reverse=True)


    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def addItem():
        title = request.form.get('title')
        add_item(title)
        return redirect(url_for('index'))


@app.route('/complete', methods=['POST'])
def completeItem():
        item = get_item(request.form['completeBtn'])
        item['status'] = "Completed"
        save_item(item)
        return redirect(url_for('index'))


@app.route('/undocomplete', methods=['POST'])
def undoCompleteItem():
        item = get_item(request.form['uncompleteBtn'])
        item['status'] = "Not Started"
        save_item(item)
        return redirect(url_for('index'))

@app.route('/remove', methods=['POST'])
def removeItem():
        item = get_item(request.form['removeBtn'])
        remove_item(item)
        return redirect(url_for('index'))
