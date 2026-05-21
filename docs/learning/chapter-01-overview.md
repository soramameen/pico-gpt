# Chapter 1: 全体像

## 目的
このリポジトリの各ディレクトリの役割を説明できるようになる。

## 対象ファイル
- `README.md`

## 理論
- GPT学習では、モデル本体・tokenizer・学習・推論を分けて見ると理解しやすい。
- 「次のtoken予測」は、学習・推論・評価の全てに関わる共通テーマ。

## コード読解メモ
- `src/`: モデル本体
- `training/`: 学習スクリプト
- `cli/`, `app.py`: 推論インターフェース
- `tests/`: 動作確認
- `datasets/`: 学習データ

## 演習
1. `README.md` を読んで、各ディレクトリの役割を自分の言葉で1行ずつ書く。
2. 「モデル」「tokenizer」「学習」「推論」の4区分で、ファイルを分類する。
3. このプロジェクトで最初に読みたいファイルを1つ選び、その理由を書く。

## 自分の言葉での要約

このプロジェクトは、Transformer アーキテクチャの LLM の仕組みを学ぶための最小 GPT 実装である。
`datasets` のテキストを tokenizer で token 化し、モデルに埋め込み・attention などの処理を通して次 token を予測する。
学習では正解との差からパラメータを更新し、保存した学習済みパラメータを `cli` や `app.py` から読み込むことで、LLM のようなテキスト生成ができる。

### 役割整理
- `src/`: モデル本体と tokenizer 実装
- `training/`: 学習を実行するスクリプト
- `cli/`, `app.py`: 学習済みモデルを使う推論インターフェース
- `datasets/`: 学習元データ
- `models/`: 学習済み checkpoint と tokenizer 保存先
- `tests/`: 動作確認

### 4区分での分類
- モデル: `src/pico_gpt.py`
- tokenizer: `src/tokenizer.py`
- 学習: `training/train_conversation.py`
- 推論: `app.py`, `cli/cli_client.py`, `cli/generate.py`

## Zenn向けメモ
- 学習時は各位置の「次 token」をまとめて予測して loss を取る
- 推論時は最後の位置の予測だけ使って 1 token ずつ伸ばす
- `generate()` は外から呼ぶ入口で、内部では `forward()` を何度も使う
