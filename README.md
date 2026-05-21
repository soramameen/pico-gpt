# 🤖 Pico-GPT

PyTorch で GPT（Generative Pre-trained Transformer）アーキテクチャを学ぶための、ミニマルで教育向けの実装です。構成は整理されており、コードを通して GPT モデルの内部動作を理解しやすくなっています。

## 🌟 特徴

- **完全な GPT アーキテクチャ**: Multi-head self-attention、position embeddings、layer normalization を実装
- **プロフェッショナルな構成**: `src/`、`training/`、`cli/`、`tests/` など用途ごとに整理
- **複数のインターフェース**: 対話型 CLI、Gradio Web アプリ、直接生成、Python API
- **最適化された学習**: 高速な会話モデル学習（16 秒）
- **GPU アクセラレーション**: CUDA を自動検出して利用
- **設定可能なモデル**: 層数、head 数、埋め込み次元を簡単に調整可能
- **テキスト生成**: temperature と top-k sampling による自己回帰生成
- **Web インターフェース**: 配布や共有がしやすい Gradio アプリ
- **Hugging Face 連携**: モデルのアップロードとデプロイ用スクリプトを同梱
- **教育向けサンプル**: 充実した例とドキュメント

## 🚀 ライブデモ

**デプロイ済みモデルを試す:** [Pico-GPT Conversational on Hugging Face](https://huggingface.co/jemico/pico-gpt-conversational)

## 📋 要件

- Python 3.7+
- PyTorch 1.12.0+
- NumPy 1.21.0+
- Regex 2022.1.18+

## 📁 プロジェクト構成

```text
pico-gpt/
├── 📁 src/                      # コア実装
│   ├── pico_gpt.py             # メイン GPT モデルとアーキテクチャ
│   ├── tokenizer.py            # Simple / BPE tokenizer
│   ├── fast_tokenizer.py       # 最適化された GPT-2 風 tokenizer
│   └── __init__.py
│
├── 📁 training/                 # 学習スクリプト
│   └── train_conversation.py   # 🌟 BEST: 会話モデルの学習
│
├── 📁 cli/                      # ユーザーインターフェース
│   ├── cli_client.py           # 🌟 MAIN: 対話型チャット CLI
│   └── generate.py             # シンプルなテキスト生成
│
├── 📁 models/                   # 学習済みモデル
│   └── pico_gpt_conversation.pt # 🌟 会話モデル（26.2M params）
│
├── 📁 datasets/                 # 学習データと tokenizer
│   ├── clean_conversation_data.txt      # 🌟 クリーンなチャットデータ
│   ├── fast_tokenizer_gpt2_8000.pkl    # 🌟 最適化 tokenizer
│   ├── combined_enhanced_data.txt       # 拡張学習データ
│   ├── comprehensive_conversations.txt  # 包括的な対話データ
│   ├── conversation_training.txt        # コア学習会話データ
│   ├── smart_reasoning_data.txt         # 高度な推論例
│   └── [other datasets...]
│
├── 📁 tests/                    # テストとサンプルスクリプト
│   ├── example.py              # 基本機能デモ
│   ├── test_conversation.py    # 会話テスト
│   ├── debug_conversation.py   # デバッグツール
│   └── test_train.py           # 学習確認
│
├── 📁 scripts/                  # ユーティリティスクリプト
│   ├── create_clean_conversation_data.py  # データ前処理
│   ├── create_conversation_data.py        # 会話データ生成
│   ├── create_smart_dataset.py           # スマートデータセット作成
│   ├── download_dataset.py               # データセット取得
│   ├── main.py                           # メインエントリーポイント
│   └── run.py                            # シンプルランナー
│
├── 📁 benchmarks/               # 性能測定
│   ├── benchmark_cuda_vs_cpu.py      # CUDA と CPU の比較
│   ├── benchmark_large_model.py      # 大規模モデル性能測定
│   └── test_large_model.py           # 大規模モデルテスト
│
├── 📄 app.py                    # 🌟 Gradio Web インターフェース
├── 📄 setup.py                  # パッケージ設定
├── 📄 requirements.txt          # Python 依存関係
├── 📄 upload_to_hf.py           # Hugging Face アップロードスクリプト
├── 📄 README.md.model           # Hugging Face model card
├── 📄 run_cli.ps1               # Windows PowerShell ランチャー
└── 📄 README.md                 # このファイル
```

## 🚀 クイックスタート

### 1. インストール

```bash
# リポジトリをクローン
git clone <your-repo-url>
cd pico-gpt

# 依存関係をインストール
pip install -r requirements.txt
```

### 2. 対話チャット（推奨）

**コマンドラインインターフェース:**
```bash
# メインスクリプト経由
python scripts/run.py
python scripts/main.py

# CLI を直接実行
python cli/cli_client.py

# Windows PowerShell
.\run_cli.ps1
```

**Web インターフェース（Gradio）:**
```bash
# ローカル Web インターフェースを起動
python app.py

# その後 http://localhost:7860 を開く
```

**対話型 CLI の機能:**
- 💬 **Conversation Mode** - やり取りをまたいで文脈を保持
- 🔄 **Single-Prompt Mode** - 独立したテキスト生成
- ⚙️ **Adjustable Settings** - temperature、top-k、max tokens を調整可能
- 📝 **Command System** - `/help`、`/settings`、`/clear` など
- 💾 **History Support** - readline による履歴サポート

### 3. モデルを学習する

```bash
# 会話モデルを学習
python training/train_conversation.py
```

### 4. テキストを生成する

```bash
# シンプルな生成
python cli/generate.py --prompt "Hello world"

# パラメータ付き生成
python cli/generate.py --prompt "Python is" --max_tokens 50 --temperature 0.8 --top_k 10

# scripts ディレクトリ経由
python scripts/main.py generate --prompt "Once upon a time"
```

### 5. 実装をテストする

```bash
# 基本機能テスト
python tests/example.py

# 学習テスト
python tests/test_train.py
```

### 6. Hugging Face にデプロイする

```bash
# model card とアップロード手順を生成
python upload_to_hf.py

# 生成された手順に従ってモデルをアップロード
```

## 💾 モデルファイル

### **Active Models**
- **`pico_gpt_conversation.pt`** - **主要な会話モデル**
  - 26.2M parameters（8 layers、8 heads、512 embedding dim）
  - CLI で使われる**デフォルトモデル**
  - 自然な会話向けに最適化

- **`pico_gpt_large.pt`** - **高性能な大型モデル**
  - 88.9M parameters（12 layers、12 heads、768 embedding dim）
  - 最大クラスのモデル性能
  - より複雑なタスク向け

### **モデル比較**
| Model | Parameters | Size | Use Case |
|-------|------------|------|---------|
| `pico_gpt_conversation.pt` | 26.2M | ~100MB | 🌟 **会話向けに最適** |
| `pico_gpt_large.pt` | 88.9M | ~350MB | 最大性能、複雑なタスク向け |

## 🎯 コマンドラインインターフェース

### 対話型 CLI コマンド

会話モード中に使えるコマンド:

- `/help` - コマンド一覧を表示
- `/settings` - 生成パラメータを表示/変更
- `/clear` - 画面をクリア
- `/reset` - 会話コンテキストをリセット
- `/status` - 会話状態を表示
- `/mode` - 会話/単発プロンプトモードを切り替え
- `/info` - モデル情報を表示
- `/load` - 別のモデルを読み込む
- `/quit` - 終了

### CLI のコマンドラインオプション

| Option | Description | Default |
|--------|-------------|---------|
| `--model` / `-m` | モデルファイルのパス | `pico_gpt_conversation.pt` |
| `--device` / `-d` | 使用デバイス（cpu/cuda/auto） | `auto` |
| `--max-tokens` / `-t` | 生成する最大トークン数 | `100` |
| `--temperature` / `-T` | Sampling temperature | `0.8` |
| `--top-k` / `-k` | Top-k sampling | `20` |
| `--prompt` / `-p` | 単発プロンプトモード | None |

### 例

```bash
# 対話型会話
python cli/cli_client.py

# Windows PowerShell でカスタム設定
.\cli\run_cli.ps1 -Model "pico_gpt_large.pt" -MaxTokens 200 -Temperature 0.9

# 創作向け（高 temperature）
python cli/generate.py --prompt "Once upon a time" --temperature 1.2 --max_tokens 200

# 事実寄り補完（低 temperature）
python cli/generate.py --prompt "Python is a programming language" --temperature 0.3

# 別モデルを使う
python cli/cli_client.py --model models/pico_gpt_conversation.pt --prompt "Test conversation"
```

## 🔧 設定

### モデルアーキテクチャ

`src/pico_gpt.py` の `GPTConfig` クラスを編集するか、カスタム設定を作成します:

```python
from src.pico_gpt import GPTConfig

# Small model（高速学習）
config = GPTConfig()
config.block_size = 256      # コンテキスト長
config.vocab_size = 50304    # 語彙サイズ
config.n_layer = 6           # transformer 層数
config.n_head = 6            # attention head 数
config.n_embd = 384          # 埋め込み次元
config.dropout = 0.2         # dropout 率

# Tiny model（超高速）
config.n_layer = 2
config.n_head = 2
config.n_embd = 64
```

### 学習パラメータ

異なる設定で学習したい場合は学習スクリプトを調整してください:

```python
# 学習ハイパーパラメータ
batch_size = 16             # バッチサイズ
learning_rate = 3e-4        # 学習率
max_iters = 5000            # 学習反復回数
eval_interval = 1000        # 検証頻度
```

## 🌐 Web インターフェース

Gradio の Web インターフェースを使うと、簡単にチャット UI を利用できます:

```bash
# Web インターフェースを起動
python app.py
```

**機能:**
- 対話型チャットインターフェース
- temperature とトークン長の調整
- リアルタイム会話
- Hugging Face Spaces へデプロイ可能

## 📚 使用例

### Python API

```python
from src.pico_gpt import GPT, GPTConfig
from src.fast_tokenizer import GPT2LikeTokenizer
import torch

# モデルを読み込む
checkpoint = torch.load('models/pico_gpt_conversation.pt', weights_only=False)
model = GPT(checkpoint['config'])
model.load_state_dict(checkpoint['model_state_dict'])
tokenizer = checkpoint['tokenizer']

# テキスト生成
model.eval()
context = torch.tensor(tokenizer.encode("Hello"), dtype=torch.long).unsqueeze(0)
generated = model.generate(context, max_new_tokens=100, temperature=0.8, top_k=10)
result = tokenizer.decode(generated[0].tolist())
print(result)
```

### カスタム学習データ

```python
# training/train_custom.py
import torch
from src.pico_gpt import GPT, GPTConfig
from src.tokenizer import SimpleTokenizer

# 自分のテキストデータを読み込む
with open('your_data.txt', 'r') as f:
    text = f.read()

# tokenizer を作成してエンコード
tokenizer = SimpleTokenizer()
data = torch.tensor(tokenizer.encode(text), dtype=torch.long)

# モデルを学習（詳細は training scripts を参照）
```

## ⚡ パフォーマンス測定

### CUDA vs CPU の性能比較

```bash
# 推論性能を計測
python benchmarks/benchmark_large_model.py

# 学習性能を比較
python benchmarks/benchmark_cuda_vs_cpu.py
```

**実行結果例（RTX 3080 Ti）:**
```text
Large Model CUDA vs CPU Inference Benchmark
============================================================
Model: 25.7M parameters (8 layers, 8 heads, 512 embedding dim)

Average Generation Time:
  CPU:  2739.40 ms
  CUDA: 430.50 ms
  Speedup: 6.36x faster

Throughput (tokens/sec):
  CPU:  18.3
  CUDA: 116.1
  Improvement: 6.36x

Memory Usage:
  CUDA Allocated: 981.1 MB
```

## 🚀 デプロイ

### Hugging Face Spaces

Web インターフェースを Hugging Face Spaces にデプロイする手順:

1. Hugging Face で新しい Space を作成
2. `app.py`、`src/`、モデルファイルをアップロード
3. ランタイムを「Python」、SDK を Gradio に設定
4. Web アプリとして公開完了

### ローカル共有

```bash
# Gradio でローカル共有
python app.py  # 共有用リンクが自動作成されます
```

## 🎓 学習メモ

### アーキテクチャ図

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                              PICO GPT ARCHITECTURE                      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                                INPUT LAYER                              │
│                                                                         │
│  Input Text: "Hello world"                                              │
│       │                                                                 │
│       ▼                                                                 │
│  ┌─────────────────┐                                                    │
│  │   TOKENIZER     │  Character/BPE tokenization                       │
│  │  SimpleTokenizer│  "Hello world" → [72, 101, 108, 108, 111, ...]    │
│  │  BPETokenizer   │                                                    │
│  └─────────────────┘                                                    │
│       │                                                                 │
│       ▼                                                                 │
│  Token IDs: [72, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]     │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           EMBEDDING LAYERS                              │
│                                                                         │
│  ┌──────────────────┐    ┌──────────────────┐                          │
│  │ Token Embedding  │    │Position Embedding│                          │
│  │    (wte)         │    │     (wpe)        │                          │
│  │  vocab_size      │    │   block_size     │                          │
│  │     ↓            │    │      ↓           │                          │
│  │  n_embd dim      │    │   n_embd dim     │                          │
│  └──────────────────┘    └──────────────────┘                          │
│            │                       │                                   │
│            └───────────┬───────────┘                                   │
│                        ▼                                               │
│                 ┌─────────────┐                                        │
│                 │  Element +  │                                        │
│                 │   Dropout   │                                        │
│                 └─────────────┘                                        │
│                        │                                               │
│                        ▼                                               │
│              Embedded Sequence                                         │
│             [batch_size, seq_len, n_embd]                             │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        TRANSFORMER BLOCKS (n_layer)                    │
│                                                                         │
│  ┌─ BLOCK 1 ──────────────────────────────────────────────────────────┐ │
│  │                                                                    │ │
│  │  Input: x                                                          │ │
│  │     │                                                              │ │
│  │     ▼                                                              │ │
│  │  ┌──────────────┐                                                  │ │
│  │  │ Layer Norm 1 │                                                  │ │
│  │  └──────────────┘                                                  │ │
│  │     │                                                              │ │
│  │     ▼                                                              │ │
│  │  ┌──────────────────────────────────────────────┐                  │ │
│  │  │         CAUSAL SELF-ATTENTION               │                  │ │
│  │  │                                             │                  │ │
│  │  │  ┌─────────┐                                │                  │ │
│  │  │  │ Q,K,V   │  Linear projection             │                  │ │
│  │  │  │ Linear  │  (n_embd → 3 * n_embd)         │                  │ │
│  │  │  └─────────┘                                │                  │ │
│  │  │      │                                      │                  │ │
│  │  │      ▼                                      │                  │ │
│  │  │  ┌─────────┐                                │                  │ │
│  │  │  │Multi-Head│  Split into n_head            │                  │ │
│  │  │  │Attention │  Compute attention weights    │                  │ │
│  │  │  │         │  Apply causal mask             │                  │ │
│  │  │  └─────────┘                                │                  │ │
│  │  │      │                                      │                  │ │
│  │  │      ▼                                      │                  │ │
│  │  │  ┌─────────┐                                │                  │ │
│  │  │  │Output   │  Concatenate heads             │                  │ │
│  │  │  │Linear   │  Project back (n_embd)         │                  │ │
│  │  │  │+Dropout │                                │                  │ │
│  │  │  └─────────┘                                │                  │ │
│  │  └──────────────────────────────────────────────┘                  │ │
│  │     │                                                              │ │
│  │     ▼                                                              │ │
│  │  ┌──────────┐    ◄── Residual Connection                           │ │
│  │  │    +     │                                                      │ │
│  │  └──────────┘                                                      │ │
│  │     │                                                              │ │
│  │     ▼                                                              │ │
│  │  ┌──────────────┐                                                  │ │
│  │  │ Layer Norm 2 │                                                  │ │
│  │  └──────────────┘                                                  │ │
│  │     │                                                              │ │
│  │     ▼                                                              │ │
│  │  ┌──────────────────────────────────────────────┐                  │ │
│  │  │                 MLP                          │                  │ │
│  │  │                                              │                  │ │
│  │  │  ┌─────────────┐                            │                  │ │
│  │  │  │   Linear    │  n_embd → 4 * n_embd       │                  │ │
│  │  │  │  (c_fc)     │                            │                  │ │
│  │  │  └─────────────┘                            │                  │ │
│  │  │         │                                   │                  │ │
│  │  │         ▼                                   │                  │ │
│  │  │  ┌─────────────┐                            │                  │ │
│  │  │  │    GELU     │  Activation function       │                  │ │
│  │  │  └─────────────┘                            │                  │ │
│  │  │         │                                   │                  │ │
│  │  │         ▼                                   │                  │ │
│  │  │  ┌─────────────┐                            │                  │ │
│  │  │  │   Linear    │  4 * n_embd → n_embd       │                  │ │
│  │  │  │ (c_proj)    │                            │                  │ │
│  │  │  │  +Dropout   │                            │                  │ │
│  │  │  └─────────────┘                            │                  │ │
│  │  └──────────────────────────────────────────────┘                  │ │
│  │     │                                                              │ │
│  │     ▼                                                              │ │
│  │  ┌──────────┐    ◄── Residual Connection                           │ │
│  │  │    +     │                                                      │ │
│  │  └──────────┘                                                      │ │
│  │     │                                                              │ │
│  │     ▼  Output to next block                                        │ │
│  └────────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  ┌─ BLOCK 2...n ────────────────────────────────────────────────────┐   │
│  │                    (Same structure)                              │   │
│  └───────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           FINAL OUTPUT LAYER                           │
│                                                                         │
│  ┌──────────────────┐                                                   │
│  │ Final Layer Norm │  Normalize final transformer output              │
│  │     (ln_f)       │                                                  │
│  └──────────────────┘                                                   │
│           │                                                            │
│           ▼                                                            │
│  ┌──────────────────┐                                                   │
│  │ Language Model   │  Linear: n_embd → vocab_size                     │
│  │ Head (lm_head)   │  Weight tied with input embeddings              │
│  └──────────────────┘                                                   │
│           │                                                            │
│           ▼                                                            │
│     Logits: [batch_size, seq_len, vocab_size]                         │
│                                                                         │
│  For Training:                    For Generation:                      │
│  ┌────────────────┐               ┌─────────────────┐                  │
│  │ Cross Entropy  │               │  Temperature    │                  │
│  │     Loss       │               │    Scaling      │                  │
│  │                │               │       │         │                  │
│  │ Compare with   │               │       ▼         │                  │
│  │ target tokens  │               │  ┌──────────┐   │                  │
│  └────────────────┘               │  │ Top-k    │   │                  │
│                                   │  │Sampling  │   │                  │
│                                   │  └──────────┘   │                  │
│                                   │       │         │                  │
│                                   │       ▼         │                  │
│                                   │  ┌──────────┐   │                  │
│                                   │  │Multinomial   │                  │
│                                   │  │ Sampling │   │                  │
│                                   │  └──────────┘   │                  │
│                                   └─────────────────┘                  │
│                                           │                            │
│                                           ▼                            │
│                                  Next Token Prediction                 │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                            KEY COMPONENTS                               │
│                                                                         │
│ Configuration (GPTConfig):                                             │
│  • block_size: 1024 (max sequence length)                             │
│  • vocab_size: 50304 (vocabulary size)                                │
│  • n_layer: 12 (number of transformer blocks)                         │
│  • n_head: 12 (number of attention heads)                             │
│  • n_embd: 768 (embedding dimension)                                  │
│  • dropout: 0.0 (dropout rate)                                        │
│                                                                         │
│ Training Components:                                                    │
│  • Training Loop: batch processing, loss calculation                   │
│  • AdamW Optimizer: weight decay regularization                        │
│  • Learning Rate Scheduling: configurable learning rate               │
│  • Validation: periodic loss evaluation                                │
│  • Checkpointing: model state saving                                   │
│                                                                         │
│ Generation Features:                                                    │
│  • Autoregressive: generates one token at a time                       │
│  • Temperature Sampling: controls randomness                           │
│  • Top-k Sampling: limits vocabulary for coherent output               │
│  • Causal Masking: prevents looking ahead during attention             │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                            DATA FLOW SUMMARY                            │
│                                                                         │
│  Text Input → Tokenization → Embeddings → Transformer Blocks →        │
│  → Layer Norm → Language Model Head → Logits → Sampling → Output      │
│                                                                         │
│  Training: Input/Target pairs, Cross-entropy loss, Backpropagation     │
│  Generation: Autoregressive sampling with temperature and top-k        │
└─────────────────────────────────────────────────────────────────────────┘
```

### アーキテクチャの理解

1. **Transformer Blocks**: 各 block は self-attention + MLP で構成
2. **Causal Attention**: 未来の token を参照できないようにする仕組み
3. **Position Embeddings**: token の順序情報を与える
4. **Layer Normalization**: 学習を安定化
5. **Weight Tying**: 入力/出力 embedding の重みを共有

### 主なコンポーネント

- `CausalSelfAttention`: masked multi-head attention を実装
- `MLP`: GELU 活性化を持つ feed-forward network
- `Block`: 完全な transformer block
- `GPT`: embeddings と language modeling head を含む全体モデル

### 学習プロセス

1. **Tokenization**: テキストを整数列へ変換
2. **Batching**: 入力/ターゲットのペアを作成
3. **Forward Pass**: 予測と損失を計算
4. **Backpropagation**: モデル重みを更新
5. **Generation**: 学習済み分布からサンプリング

## ⚡ パフォーマンス向上のヒント

### 学習を高速化するには
- `n_layer`、`n_head`、`n_embd` を小さくする
- `block_size` と `batch_size` を小さくする
- GPU が使えるなら有効化する: `device = 'cuda'`

### 生成品質を上げるには
- より長く学習する（反復回数を増やす）
- 語彙を大きくする
- モデルサイズを増やす
- temperature と `top_k` を調整する

### メモリ最適化
- メモリ不足なら batch size を下げる
- 大規模モデルでは gradient checkpointing を使う
- mixed precision training を検討する

## 🐛 トラブルシューティング

### よくある問題

**"CUDA out of memory"**
```bash
# CPU を使うか batch size を減らす
python cli/cli_client.py --device cpu
# または config でモデルサイズを小さくする
```

**"Model file not found"**
```bash
# 先にモデルを学習する
python training/train_small.py
```

**生成品質が低い**
```bash
# より長く、またはより多くのデータで学習する
# 最良の会話品質には train_final.py を使用
```

**PowerShell Execution Policy (Windows)**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## ✅ テスト結果

すべてのコア機能は検証済みです。

### 検証済み機能
✅ **Transformer Architecture** - causal masking 付き multi-head self-attention  
✅ **Training Pipeline** - 適切なデータ batching、AdamW optimizer、checkpointing  
✅ **Text Generation** - temperature/top-k sampling による自己回帰生成  
✅ **Tokenization** - 文字単位 tokenizer と BPE tokenizer  
✅ **CLI Interface** - 対話型会話モードと単発プロンプトモード  
✅ **GPU Support** - 自動検出付き CUDA アクセラレーション  

### パフォーマンス特性
- **Training Speed**: 会話モデルは 16 秒、CPU で約 143 tokens/second
- **Memory Usage**: 小規模/大規模モデルのどちらにも効率的
- **Convergence**: 良好な学習曲線を確認
- **Generation Quality**: 学習済みモデルで一貫した出力

## 📈 更新内容（リファクタ後）

### **リファクタ前** ❌
- すべてがルートフォルダに散在
- 学習スクリプトとコアコードが混在
- ナビゲーションと保守が困難
- import path が混乱

### **リファクタ後** ✅
- **Clean structure**: 論理的なフォルダ構成
- **Separated concerns**: 各フォルダの役割が明確
- **Professional**: 一般的で扱いやすいプロジェクトレイアウト
- **Maintainable**: コードを見つけやすく修正しやすい
- **Modular**: 各コンポーネントを独立して import 可能

## 📝 統合例

### Batch Scripts (Windows)
```batch
@echo off
python cli/cli_client.py --prompt "%1" --max-tokens 100 > output.txt
echo Generated text saved to output.txt
```

### PowerShell Functions
```powershell
function Generate-Text {
    param([string]$Prompt)
    python cli/cli_client.py --prompt $Prompt --max-tokens 100
}
```

## 📝 ライセンス

このプロジェクトはオープンソースで、MIT License のもとで利用できます。

## 🤝 コントリビュート

Issue、機能要望、Pull Request を歓迎します。

---

*Happy training! 🚀*

**用途例:**
- 教育用途・transformer 学習
- GPT アーキテクチャの実験  
- 小規模な言語モデリングタスク
- 研究開発
- 適切にスケールさせた本番利用
