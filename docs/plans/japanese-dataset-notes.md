# Japanese Dataset Notes

## Selected dataset
- Dataset: `shi3z/Japanese_wikipedia_conversation_100K`
- Source: Hugging Face Datasets
- License: `MIT` (要再確認: dataset card ベース)
- Shape: `conversations` 配列
- Message format: `{"from": "human"|"gpt", "value": "..."}`

## Why selected
- 日本語会話データである
- `Human:/Assistant:` 形式へ変換しやすい
- Hugging Face `datasets` で直接取得できる
- ライセンス表記が比較的明確

## Planned output
- `datasets/japanese_conversation_training.txt`
- format:
  - `Human: ...`
  - `Assistant: ...`
  - blank line separator

## Caveats
- Wikipedia由来の合成/QA寄り会話が多い可能性がある
- 雑談日本語ではなく説明・QA寄りになる可能性がある
- 最終利用前に dataset card を人間の目で再確認する
