# Chapter 5: Training

## 目的
学習スクリプトを読み、データから checkpoint 保存までの流れを説明できるようになる。

## 対象ファイル
- `training/train_conversation.py`
- 必要なら `training/train_reasoning_model.py`

## この章で見るもの
- `get_batch`
- `estimate_loss`
- learning rate schedule
- optimizer
- gradient accumulation
- checkpoint

## 理論
- 学習は input/target の対から loss を計算し、重みを更新する反復処理。
- optimizer は勾配を使ってパラメータを更新する。
- validation は過学習や改善状況の確認に使う。

## コード読解の観点
1. `x` と `y` はどう作られるか
2. `estimate_loss` はなぜ `torch.no_grad()` なのか
3. warmup / cosine decay の意図
4. checkpoint に何を保存しているか

## 演習
1. `get_batch` が返す `x, y` の意味を説明する。
2. なぜ `y` は `x` を1つずらした形なのか説明する。
3. checkpoint に tokenizer も保存する理由を考える。

## 自分の言葉での要約
- ここに自分の要約を書く

## Zenn向けメモ
- ここに Scrap 用の短い気づきを書く
