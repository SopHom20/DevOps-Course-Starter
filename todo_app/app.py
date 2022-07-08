from flask import Flask, render_template, request

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)


@app.route('/add', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        title = request.form.get('title')
        print(title)
        return '/'


