# GPT学習カリキュラム

## Chapter 1. 全体像
- 対象: `README.md`
- 目的: リポジトリの役割分担を説明できるようになる

## Chapter 2. Attention とモデル前半
- 対象: `src/pico_gpt.py`
- 目的: `GPTConfig`, `LayerNorm`, `CausalSelfAttention` を説明できるようになる

## Chapter 3. Forward / Loss / Generate
- 対象: `src/pico_gpt.py`
- 目的: `Block`, `GPT.forward()`, `generate()` を説明できるようになる

## Chapter 4. Tokenizer
- 対象: `src/tokenizer.py`, `src/modern_tokenizer.py`
- 目的: 文字列から token id になる流れを説明できるようになる

## Chapter 5. Training
- 対象: `training/train_conversation.py`
- 目的: バッチ作成、loss、optimizer、checkpoint の流れを説明できるようになる

## Chapter 6. Inference / UI
- 対象: `cli/cli_client.py`, `cli/generate.py`, `app.py`
- 目的: 学習済みモデルがどう使われるか説明できるようになる

## Chapter 7. Rebuild / Explain
- 対象: 学習ログ全体
- 目的: 最小GPTの再実装計画と Zenn 記事の骨子を作る
