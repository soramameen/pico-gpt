# GPT学習プラン

## 目的
このリポジトリ `pico-gpt` を使って、GPTの仕組みをコードを読みながら段階的に学ぶ。
理論だけでなく実際に手を動かしつつ進め、最終的には自分の理解で実装できる状態を目指す。
学習終了時には、理解の実体として「自分のリポジトリ」「自分の言葉での解説」「自分で書いた実装やノート」が残る状態を目標にする。

## 現状把握
- コア実装: `src/pico_gpt.py`
- トークナイザ: `src/tokenizer.py`, `src/modern_tokenizer.py`
- 学習スクリプト: `training/train_conversation.py`, `training/train_reasoning_model.py`
- 推論/操作: `cli/cli_client.py`, `cli/generate.py`, `app.py`
- サンプル/テスト: `tests/`
- 概要資料: `README.md`, `training/README.md`

## 学習の大きな流れ
1. プロジェクト全体像をつかむ
2. GPT本体の実装を読む
3. トークナイズの流れを理解する
4. 学習ループを読む
5. 推論・生成処理を読む
6. 自分で最小実装・説明資料・学習ログを残す

## チュートリアル案
### Day 0: 学習環境と成果物設計
- 学習の進め方を決める
- 最終成果物の形を決める
- 候補:
  - 自分用の学習リポジトリ
  - 各章の解説ノート
  - 最小GPTの再実装
  - 学習後に口頭/文章で説明できるチェックリスト
  - 将来的な `AGENTS.md` / skills 設計メモ

### Day 1: 全体像
- `README.md` をベースに構成を把握
- どのファイルが「モデル」「学習」「推論」かを整理
- GPTを構成する部品を言葉で説明する

### Day 2: モデル本体 前半
- `src/pico_gpt.py`
- 学ぶ観点:
  - `GPTConfig`
  - `LayerNorm`
  - `CausalSelfAttention`
  - attentionの入出力shape
  - causal mask の意味

### Day 3: モデル本体 後半
- `src/pico_gpt.py`
- 学ぶ観点:
  - `MLP`
  - `Block`
  - `GPT.forward()`
  - `generate()`
  - logits と loss の関係

### Day 4: トークナイザ
- `src/tokenizer.py`
- `src/modern_tokenizer.py`
- 学ぶ観点:
  - 文字列→token id
  - vocabの持ち方
  - BPE/サブワードの考え方
  - 学習時/推論時での役割

### Day 5: 学習ループ
- `training/train_conversation.py`
- 余裕があれば `training/train_reasoning_model.py`
- 学ぶ観点:
  - バッチ作成
  - loss計算
  - optimizer
  - LR schedule
  - checkpoint保存

### Day 6: 推論とUI
- `cli/cli_client.py`
- `cli/generate.py`
- `app.py`
- 学ぶ観点:
  - モデル読込
  - prompt処理
  - サンプリング
  - 会話モード

### Day 7: 再実装と説明
- 学んだ内容を元に最小実装を書く
- 自分の言葉で説明を書く
- 理解が曖昧な箇所を洗い出す
- `AGENTS.md` や skills に落とし込むなら何が必要か整理する

## 進め方
- 毎回1ファイルずつ読む
- まず役割を要約
- 次に重要クラス/関数を追う
- 最後に「このファイルでGPT理解に必要なポイント」を3〜5個に絞る
- 理論説明のあと、必ず小さな手を動かす課題を置く
- 私は答えを先に完成させすぎず、ユーザー自身が考えて実装できる余白を残す
- 受け身ではなく、毎回「自分の言葉で説明する」「自分で一部を書く」を重視する
- 1日8時間の集中学習を前提に、各日で「読む → 考える → 書く → 説明する」を回す
- 毎日の終わりに成果物を1つ残す

## 想定する最終成果物
- このリポジトリ内で整理された学習ログ / チュートリアル / 実装メモ
- Zenn (`zenn.dev`) 用の最終記事草案
- 学習途中で使う Zenn Scrap メモ

## TODO
- [x] リポジトリの主要ファイルを確認する
- [x] 初回学習プランを作る
- [x] 学習ゴール（理論＋手を動かす＋自力実装重視）を確定する
- [x] 前提知識（PyTorch / Transformer / 数学）の現在地を確認する
- [x] 1回あたりの学習ペースを決める（1日8時間集中）
- [x] 最終成果物の構成を決める（このリポジトリ + Zenn Scrap + 最終記事）
- [x] チュートリアル形式を決める（章ごとの教科書形式）
- [x] Zenn最終記事の方向を決める（学習記録寄り）
- [x] 学習ログの配置先を決める（`docs/learning/*`）
- [x] チュートリアルの章立てを確定する
- [x] 最初に読むファイルを決める
- [x] Day 1 を開始する
- [x] Chapter 1 の全体像確認を完了する
- [ ] Apple Silicon / MPS 対応方針を決める
- [ ] MPS 対応の影響範囲を洗い出す
- [ ] 実装前に最小変更案を確定する

## Apple Silicon / MPS 対応メモ
### 目的
- M4 Mac で `cpu` 固定になっている箇所を見直し、`mps` が使えるなら推論・学習を高速化したい。

### 現状のローカル調査
- `cli/generate.py`
  - device 判定が `cuda` / `cpu` の2択。
  - `torch.load(..., map_location='cpu')` で固定ロードしている。
- `cli/cli_client.py`
  - device 判定が `cuda` / `cpu` の2択。
  - `torch.load(..., map_location=self.device)` なので `mps` を渡せれば比較的対応しやすい。
- `app.py`
  - device 判定が `cuda` / `cpu` の2択。
  - `torch.load(..., map_location='cpu')` 固定。
- `training/train_conversation.py`
  - device 判定が `cuda` / `cpu` の2択。
  - AMP を `cuda` 前提で使っている (`torch.cuda.amp.GradScaler`, `autocast`)。
  - そのため、推論より学習側の方が MPS 対応の考慮点が多い。

### ざっくり方針案
1. まずは共通の device 選択ロジックを決める。
   - 優先順位案: `cuda` → `mps` → `cpu`
2. 推論系から先に対応する。
   - `cli/generate.py`
   - `cli/cli_client.py`
   - `app.py`
3. 学習系は別ステップで対応する。
   - `training/train_conversation.py`
   - `training/train_reasoning_model.py`
4. `cuda` 専用最適化は `device == 'cuda'` のときだけ有効にする。
   - AMP / GradScaler など
5. `torch.load(..., map_location='cpu')` 固定箇所は、ロード後に `model.to(device)` する方式を維持するか、`map_location=device` に寄せるかを決める。

### リスク / 未確認事項
- この plan mode では外部Web調査が制限されており、PyTorch MPS の最新制約までは未確認。
- `torch.cuda.amp.*` は MPS ではそのまま使えない可能性が高い。
- 一部演算が MPS 未対応なら、学習時に別エラーが出る可能性がある。
- `scaled_dot_product_attention` や `torch.multinomial` などが MPS 上で安定動作するかは実機確認が必要。

### 実装するとしたら最小変更候補
- 共通 helper 追加:
  - `if torch.cuda.is_available(): return 'cuda'`
  - `elif torch.backends.mps.is_available(): return 'mps'`
  - `else: return 'cpu'`
- 推論系3ファイルの device 選択を helper に寄せる。
- 学習系は `use_amp = (device == 'cuda')` を維持しつつ、`device` 自体は `mps` を許可する。
- まずは推論で `mps` 動作確認、その後に学習確認。

## ユーザーに確認したいこと
1. 最初の入口はどれがよさそうですか？
   - a. `README.md` から全体像
   - b. `src/pico_gpt.py` から本体
   - c. まずチュートリアルの目次を固める
2. `docs/learning/*` に置く内容はどこまで含めますか？
   - a. 読書メモだけ
   - b. 読書メモ + 演習課題
   - c. 読書メモ + 演習課題 + Zenn下書き断片
3. 章ごとの教科書形式は、各章の最後に演習を置く形でよいですか？
   - a. はい
   - b. いいえ

## 日本語対話データ導入プラン
### 目的
- インターネット上のオープンな日本語対話データを取得し、`pico-gpt` の学習に使える `datasets/*.txt` 形式へ変換し、最終的に `training/train_conversation*.py` で学習できる状態まで持っていく。

### ゴール定義
- データ取得元が決まっている
- ライセンス確認メモが残っている
- 取得スクリプトまたは取得手順が再現可能
- `Human: ...\nAssistant: ...` 形式の学習用 `.txt` が `datasets/` に配置されている
- 学習スクリプトがその新データを読める
- 少なくとも短時間学習 (`train_conversation_quick.py` 相当) で 1 回動作確認できる

### 前提として分かっていること
- 既存の会話学習データは `datasets/large_conversation_training.txt`
- 学習スクリプトはこの `.txt` を直接読んで token 化している
- 既存コード/スクリプトでも `Human:` / `Assistant:` 形式が前提になっている
- `scripts/build_conversation_corpus.py` には Hugging Face `datasets` を使って会話データを取り込み、`Human:/Assistant:` 形式へ整形する発想がすでにある

### 候補データセットの選定基準
1. オープンライセンスであること
2. 日本語テキストが十分に含まれること
3. できれば対話形式、少なくともユーザー/応答のペアへ変換しやすいこと
4. Hugging Face `datasets` で取得しやすいこと
5. 学習用途・再配布条件が明確であること

### 実行プラン
#### Phase 1: 候補探索とライセンス確認
- Hugging Face 上の日本語対話データ候補を 3〜5 個洗い出す
- 各候補について以下を確認する
  - データセット名
  - 概要
  - ライセンス
  - 会話形式かどうか
  - レコード構造（instruction / input / output, messages, prompt / response など）
- ここで 1 個に絞る

#### Phase 2: 取り込み方針の決定
- 取得方法を決める
  - 例: `datasets.load_dataset(...)`
- 保存先ファイル名を決める
  - 例: `datasets/japanese_conversation_training.txt`
- 整形ルールを決める
  - 基本形式: `Human: {user_text}\nAssistant: {assistant_text}\n\n`
- クリーニング方針を決める
  - 空文字の除外
  - 極端に長いサンプルの除外
  - 重複削除
  - 日本語比率が極端に低いサンプルの除外（必要なら）

#### Phase 3: 取得・整形スクリプト作成
- `scripts/` 配下に日本語対話データ取り込み用スクリプトを追加する
  - 仮名: `scripts/build_japanese_conversation_corpus.py`
- 処理内容
  - Hugging Face から dataset 取得
  - 必要な split を読む
  - 1件ごとに user / assistant のペアへ変換
  - `Human:` / `Assistant:` 形式で `.txt` に追記
  - 件数・スキップ件数・出力文字数を最後に表示

#### Phase 4: 学習スクリプト接続
- 既存 `train_conversation.py` を直接変えるか、別ファイル化するか決める
- 学習用データパスを新データへ向ける
  - 例: `datasets/japanese_conversation_training.txt`
- まずは quick 版で短時間確認する
  - 既存の `train_conversation_quick.py` をベースにする方が安全

#### Phase 5: 動作確認
- データ生成スクリプトを実行して `.txt` を作る
- 先頭数件を読んで形式確認する
- quick 学習を回す
- `cli/generate.py` で日本語 prompt を試す
  - 例: `Human: おはよう\nAssistant:`
- 出力が完全でなくても、日本語会話形式へ少し寄るか観察する

### 実装時の変更候補
- 新規: `scripts/build_japanese_conversation_corpus.py`
- 必要なら新規: `training/train_conversation_ja_quick.py`
- 必要なら更新: `README.md` or `datasets/README.md` にデータ取得方法メモ
- 必要なら更新: `docs/learning/*` に学習ログ追加

### リスク
- ライセンス条件が曖昧な dataset は採用できない
- 日本語対話でも instruction tuning 形式だと、純粋な雑談対話とは少し分布が違う
- データ量が多すぎると tokenization / 学習時間が伸びる
- 日本語と英語が混ざる dataset の場合、英語寄り出力が残る可能性がある

### 完了条件
- オープンな日本語対話データをネットから取得する手順が再現可能
- `datasets/` に学習可能な `.txt` が生成される
- quick 学習が 1 回通る
- `cli/generate.py` で日本語 prompt を投げて出力確認できる

### TODO（日本語データ導入）
- [ ] 候補 dataset を 3〜5 個洗い出す
- [ ] ライセンス確認メモを残す
- [ ] 1 個選定する
- [ ] 取り込みスクリプトの入出力仕様を決める
- [ ] `.txt` のフォーマットを決める
- [ ] データ取得・整形スクリプトを実装する
- [ ] `datasets/` に日本語会話コーパスを生成する
- [ ] quick 学習スクリプトで動作確認する
- [ ] 日本語 prompt で推論確認する

## 次の候補アクション
- A. 日本語対話データの候補探索から始める
- B. 既存 `scripts/build_conversation_corpus.py` の構造を読んで再利用方針を決める
- C. `.txt` の最終フォーマット仕様を先に固める

## 学習スタイルの合意
- 理論と実装を両方やる
- 手を動かしながら学ぶ
- 実装の主体はユーザー自身
- 私は整理・問いかけ・レビュー・ヒント提供を担当する
- 学習後に理解の実体が残るように進める
- チュートリアルは章ごとの教科書形式で進める
- 外部公開を意識し、Zenn Scrap に途中メモを残し、最後に学習記録寄りの長めの記事へ育てる
- 学習ログは `docs/learning/*` に整理する
- このリポジトリ内の学習記録と記事が相互に補完する形で整理する
