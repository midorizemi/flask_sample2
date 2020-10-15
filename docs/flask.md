## flask CLI

flask run のためには，環境変数FLASK_APPの定義が必要．
FLASK_APPは，Flaskインスタンスを指定する．
本リポジトリでは，apiプロジェクトはPythonパッケージとして定義しているため，
```sh
pip install -e .  ;:setup.pyを実行する
export FLASK_APP=api.application:app
flask run
```
とする必要がる．

もし，Python -m で事項する場合は，apiプロジェクトの`__main__.py`を実行する.

```sh
python -m api
```

## DBの準備
DBクライアントはPyMysqlパッケージを利用  
ORMとしてはSQLAlchemyを利用
マイグレーションは Flask-Migrateを利用

DBの接続情報は，環境変数で指定できる．

```
DB_USER=root
DB_PASSWORD=root
DB_HOST=localhost
DB_DATABASE=test_flask_sample

##

UUID: （Universally Unique Identifier）とは、ソフトウェア上でオブジェクトを一意に識別するための識別子である


## GCP FunctionでFlaskを使うとき
基本的には，1ファンクション1モジュールであると考える． [詳細](https://cloud.google.com/functions/docs/writing?hl=ja#functions-writing-helloworld-http-python)
flaskのrequestモジュールはGCPですでにインポート済み


```python
from flask import escape, helper

def api_function(request):
    return something
```


Runtime はPython 3.7, 3.8をサポートしている． [ランタイムについて]()
また，GCP FunctionsのデフォルトのPythonパッケージは以下の通り．
[依存関係](https://cloud.google.com/functions/docs/writing/specifying-dependencies-python?hl=ja)

```requirements.txt
aiohttp==3.6.2
async-timeout==3.0.1
attrs==19.3.0
cachetools==4.1.1
certifi==2020.6.20
chardet==3.0.4
click==7.1.2
Flask==1.1.2
google-api-core==1.21.0
google-api-python-client==1.10.0
google-auth==1.19.2
google-auth-httplib2==0.0.4
google-cloud-core==1.3.0
google-cloud-trace==0.23.0
googleapis-common-protos==1.52.0
grpcio==1.30.0
httplib2==0.18.1
idna==2.9
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
multidict==4.7.6
opencensus==0.7.9
opencensus-context==0.1.1
pip==20.1.1
protobuf==3.12.2
pyasn1==0.4.8
pyasn1-modules==0.2.8
pytz==2020.1
PyYAML==5.3.1
requests==2.24.0
rsa==4.6
setuptools==47.3.1
six==1.15.0
uritemplate==3.0.1
urllib3==1.25.9
Werkzeug==1.0.1
wheel==0.34.2
wrapt==1.12.1
yarl==1.5.1
```


### GCP SQL と Flask on GCP Functionのやり方．

current_appを呼び出すらしい．．
https://stackoverflow.com/questions/53822809/how-can-i-use-flask-sqlalchemy-with-google-cloud-functions

### GCP FunctionsとFlaskメソッド
GCPの方でリポジトリにデプロイするとそのまま，main.pyで定義されているメソッドが
APIのファンクションに変更されるため，切り分けるなどは特には必要ない．


懸念：main.pyが長くなるので切り分けたほうが良さげかなと思う．


### 環境変数に専用項目の値を入れるように構成を変更

SQL系はGCPの方でソケットが指定されているので，環境別で切り分けられるように
config.pyなどの工夫が必要．

循環import回避のためのディレクトリ構成の参考：[cookiecutter-flask](https://github.com/cookiecutter-flask/cookiecutter-flask)


### サービスが依存するサービス

ロギング
Error管理など
画像，動画の配信CDN
キャッシュなど
GCPのサービスを考える．


### FlaksのConfigについて

参考：[いまさらながら Flask についてまとめる 〜Configuration〜](https://www.subarunari.com/entry/2018/03/17/%E3%81%84%E3%81%BE%E3%81%95%E3%82%89%E3%81%AA%E3%81%8C%E3%82%89_Flask_%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6%E3%81%BE%E3%81%A8%E3%82%81%E3%82%8B_%E3%80%9CConfiguration%E3%80%9C)
参考： [公式 Configuration](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/config.html)


### 機能の分割

Flaskが提供しているBluePrintを利用する．
- [参考](https://qiita.com/shimajiri/items/fb7d1d58de0b0d171c88)
- [公式参考](https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/blueprints.html#blueprints)