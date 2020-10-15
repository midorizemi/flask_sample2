# イディオムメモ
忘れているのでメモ

## 内包表示

```python
array = [ n for n in range(1,101)] # 1-100の整数リストを生成
# => [1,2,3...100]
type(array)
# => <class 'list'>

# Dictionaryオブジェクトから 値がNoneでない keyのリストを取得する
keys = [ k for k, v in dictionaries if v is not None]
```

- ジェネレータ内包表記

内包表記に`[]` ではなく`()` を使った場合，
参照時に逐次評価するジェネレータオブジェクトを生成する．

```python
gen = (a % 3 for a in range(0, 10000000)) # rangeに当たる要素，リストインスタンスが巨大になってしまうとき，もしくは無限大リストを使いたいときに利用する．

print(gen.__next__())
```

Python3の場合，参照は `__next__()` を利用する


## コマンド

### python コマンド
#### オプション

- -m  
> run library module as a script (terminates option list)

Python モジュールパスにあるモジュールを指定された場合、そのモジュールをスクリプトとして実行します。

### flake8 コマンド

コーディング規約を矯正してくれるやつ

### yapf コマンド

Google製のコーディング規約に沿ってプログラムを修正してくれるやつ．