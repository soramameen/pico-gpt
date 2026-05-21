# Chapter 4: Tokenizer

## 目的
文字列が token id に変換される流れを理解し、モデルが生の文字列を直接読んでいないことを説明できるようになる。

## 対象ファイル
- `src/tokenizer.py`
- `src/modern_tokenizer.py`

## この章で見るもの
- encode / decode
- vocab
- BPE 的な考え方
- tokenizer と model の接続

## 理論
- モデルは整数列を受け取る。
- tokenizer は文字列と token id の橋渡し。
- vocab の設計は学習効率と表現力に影響する。

## コード読解の観点
1. どの tokenizer がどこで使われているか
2. encode / decode の責務
3. vocab size が config とどう結びつくか

## 演習
1. 同じ文章を tokenizer で token にしたとき何が起きるか確認する。
2. なぜ decode が必要か説明する。
3. vocab size を変えると何が影響を受けそうか考える。

## 自分の言葉での要約
- ここに自分の要約を書く

## Zenn向けメモ
- ここに Scrap 用の短い気づきを書く
