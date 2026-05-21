# Chapter 3: Forward / Loss / Generate

## 目的
`Block`, `GPT.forward()`, `generate()` を追い、学習時と推論時の流れの違いを説明できるようになる。

## 対象ファイル
- `src/pico_gpt.py`

## この章で見るもの
- `MLP`
- `Block`
- `GPT.forward()`
- `loss`
- `generate()`
- temperature / top-k / top-p

## 理論
- Transformer block は attention と MLP を residual connection で積み重ねる。
- 学習時は logits と targets から loss を計算する。
- 推論時は最後の token の logits から次 token をサンプリングする。

## コード読解の観点
1. `Block.forward()` の residual connection を追う
2. `targets is not None` で何が変わるか
3. なぜ推論時は `x[:, [-1], :]` を使うのか
4. `generate()` の各引数が出力にどう効くか

## 演習
1. `forward()` の学習時/推論時の分岐を図にする。
2. `logits` と `loss` の関係を言葉で説明する。
3. temperature を上げ下げすると何が起きるか説明する。

## 自分の言葉での要約
- ここに自分の要約を書く

## Zenn向けメモ
- ここに Scrap 用の短い気づきを書く
