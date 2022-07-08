from flask import Flask, render_template, request, redirect, url_for

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item, get_item, save_item

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)



@app.route('/add', methods=['POST'])
def addItem():
    if request.method == 'POST':
        title = request.form.get('title')
        add_item(title)
        return redirect(url_for('index'))

@app.route('/complete', methods=['GET', 'POST'])
def completeItem():
    if request.method == 'POST':
        item = get_item(request.form['completeBtn'])
        item['status'] = "Complete"
        save_item(item)
        return redirect(url_for('index'))

@app.route('/undocomplete', methods=['GET', 'POST'])
def undoCompleteItem():
    if request.method == 'POST':
        item = get_item(request.form['uncompleteBtn'])
        item['status'] = "Not Started"
        save_item(item)
        return redirect(url_for('index'))

