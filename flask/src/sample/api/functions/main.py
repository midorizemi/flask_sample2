from flask import Blueprint
from markupsafe import escape
from flask import request
from flask import jsonify
from api.database import db
from .models.user import User, UserSchema

# Blueprintのオブジェクトを生成する
app = Blueprint('functions', __name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    if request.method == 'POST':
        return '{} is posted'.format(escape(post_id))
    else:
        return 'Post is {}'.format(escape(post_id))


@app.route('/users/')
def users():
    all_user = User.query.all()
    return jsonify({
        'status': 'ok',
        'users': UserSchema(many=True).dump(all_user)
    })


@app.route('/add/')
def add_user():
    peter = User(name='Tester',
                 address='東京都多摩市てすと1－1－1',
                 tel='000-000-0000',
                 mail='test@local.co.jp')
    db.session.add(peter)
    db.session.commit()
    return jsonify({'status': 'ok', 'user': UserSchema().dump(peter)})
