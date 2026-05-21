# Chapter 6: Inference / UI

## 目的
学習済みモデルが CLI やアプリからどう呼ばれるかを理解する。

## 対象ファイル
- `cli/cli_client.py`
- `cli/generate.py`
- `app.py`

## この章で見るもの
- checkpoint 読み込み
- prompt 処理
- conversation mode
- generation parameter

## 理論
- 学習済みモデルは推論時に checkpoint から復元される。
- UI はモデルそのものではなく、入力整形と出力表示の責務を持つ。

## コード読解の観点
1. モデルと tokenizer をどう読み込むか
2. prompt がどう token 化されるか
3. 会話履歴をどう扱うか

## 演習
1. CLI の責務と model の責務を分けて説明する。
2. 会話モードと単発生成モードの違いを書く。
3. `max_tokens`, `temperature`, `top_k` をどう調整したいか自分なりに考える。

## 自分の言葉での要約
- ここに自分の要約を書く

## Zenn向けメモ
- ここに Scrap 用の短い気づきを書く
