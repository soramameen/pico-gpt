# Session State

このファイルは、セッションが変わっても前回の続きから再開するための状態管理ファイル。

## 現在の章
- Chapter 1: 全体像（完了）
- 次候補: Chapter 2: Attention とモデル前半

## 現在の状態
- Chapter 1 の全体像把握を完了
- `generate.py` / `train_conversation.py` / `src/pico_gpt.py` を入口として学習と推論の流れを確認済み
- 学習済み checkpoint の保存と推論実行を実際に確認済み
- Apple Silicon / MPS 対応の最小実装を追加済み

## 直前に終わったこと
- `README.md` を読んでディレクトリの役割を整理
- `forward` と `generate` の役割を区別して確認
- `training/train_conversation.py` を実行し、`models/pico_gpt_conversation.pt` の生成を確認
- `cli/generate.py --model models/pico_gpt_conversation.pt --prompt "hello"` で推論確認
- `src/device_utils.py` を追加し、推論/学習の device 選択を `cuda -> mps -> cpu` に対応

## 次にやること
1. Chapter 2 として `src/pico_gpt.py` の `GPTConfig`, `LayerNorm`, `CausalSelfAttention` を読む
2. M4 Mac 上で `mps` が選ばれるか実機確認する
3. 必要なら `docs/learning/chapter-01-overview.md` の要約を清書する
4. 必要なら `docs/learning/zenn-notes.md` に Chapter 1 の気づきを短く追加する

## 次回開始用プロンプト
- `docs/learning/session-state.md` を読んで、Chapter 2 を始めつつ MPS 対応の動作確認も進めてください。

## 未解決・保留
- MPS 上で学習ループが最後まで安定するかは未確認
- `torch.cuda.amp.*` を使う箇所は CUDA 専用最適化のまま
- どの粒度で Zenn Scrap を毎回書くかは運用しながら調整
