---
name: gpt-learning-chapter
description: Guide one chapter of GPT study in this repository when the user wants to learn theory and implementation together, produce notes in docs/learning, and keep ownership of the implementation.
---

# GPT Learning Chapter

Use this skill when progressing one chapter of the GPT tutorial in this repository.

## Instructions
- Start from `docs/learning/curriculum.md` and the target chapter file in `docs/learning/`.
- Read the relevant source files before explaining.
- Explain in Japanese unless the user requests another language.
- Keep the user as the primary implementer; prefer questions, checkpoints, and small exercises over full solutions.
- For each chapter, produce this flow:
  1. 目的を1-3文で確認
  2. 対象コードの役割を要約
  3. 理論と実装の対応を示す
  4. 小さな演習を出す
  5. `docs/learning/...` に学習ログを残す案を示す
- When useful, propose a short Zenn Scrap note extracted from the lesson.
