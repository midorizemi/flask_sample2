from flask import Flask, url_for
app = Flask(__name__)

"""
ruteを定義するデコレータ
@app.route()を利用してAPIのURLを定義する．
"""

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

"""
ruteに変数を与えたい場合，<valiable_name>を引数に与える必要がある．
また，コンバータが用意されており，変数の型を指定できる．
"""
from markupsafe import escape # markupsafeはflaskがデフォルトでサポートしているインジェクション攻撃を回避するための依存パッケージ

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

"""
ルーティングの最後の '/'について
最後に/をつけると，
/xxxx でサーバにリクエストをなげた際に，/xxxx/ にリダイレクトする．
/なしでルーティングを定義して /yyyy/にリクエストを投げると404ErrorをFlaskは返す．
つまり最後の/つきURLは明確な違いがあることに注意
"""
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

"""
urlのこうちく
"""

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Doe'))

"""
HTTP メソッドを定義したいときは，methodsオプションにHTTPメソッド名をリストで与える
"""

from flask import request

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    if request.method == 'POST':
        return '{} is posted'.format(escape(post_id))
    else:
        return 'Post is {}'.format(escape(post_id))

"""
requet について

HTTPリクエストオブジェクトを扱いたい場合は， requestモジュールをインポートする必要がある．
APIセクションにて詳細あり．
ひとまず，よく利用するものとして，以下がある．
HTTPリクエストメソッドを持つ：method属性
formから送られてきたデータ,例えば，Post，Putリクエストで送信されるデータ）は：form属性
URL中のパラメータは：args属性となっている．

以下例

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']): # もし，form属性にKeyが存在しない場合は，KeyErrorが発生する．Errorキャッチもできるし，HTTP 400 Bad RequestをFlaskが返す．
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    searchword = request.args.get('key', '') # args属性を参照する場合は，getメソッドを利用する． KeyErrorは発生しない代わりに，第2引数が与えられる．
    return render_template('login.html', error=error)
"""


# if __name__ == '__main__':
#     app.run()