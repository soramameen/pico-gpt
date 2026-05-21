# Chapter 2: Attention とモデル前半

## 目的
`src/pico_gpt.py` の前半を読み、GPT の基本部品と self-attention の役割を説明できるようになる。

## 対象ファイル
- `src/pico_gpt.py`

## この章で見るもの
- `GPTConfig`
- `LayerNorm`
- `CausalSelfAttention`
- RoPE
- attention の shape
- causal mask

## 理論
- GPT は token 列を受け取り、各 token が過去の token を見ながら次を予測する。
- self-attention は「どの過去 token をどれだけ参照するか」を重みとして計算する。
- causal mask は未来の token を見ないための制約。
- multi-head attention は複数の見方を並列に持つ。

## コード読解の観点
1. `GPTConfig` にどんなハイパーパラメータがあるか
2. `LayerNorm` は何を正規化しているか
3. `CausalSelfAttention.forward()` の入力と出力の shape
4. `q, k, v` がどこで作られるか
5. mask がどの条件で適用されるか

## 演習
1. `config.n_embd % config.n_head == 0` が必要な理由を書く。
2. `q`, `k`, `v` の shape を `B, T, C` から追跡する。
3. causal mask がないと何が問題か説明する。
4. `use_rope` が true のとき、位置情報はどこで入るか確認する。

## 自分の言葉での要約
- ここに自分の要約を書く

## Zenn向けメモ
- ここに Scrap 用の短い気づきを書く
