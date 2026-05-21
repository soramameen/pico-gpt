---
name: zenn-learning-log
description: Turn GPT study notes in docs/learning into short Zenn Scrap entries or a learning-record-style article outline when the user wants to publish progress externally.
---

# Zenn Learning Log

Use this skill when converting repository study notes into Zenn-ready writing.

## Instructions
- Read the relevant files in `docs/learning/` first.
- Preserve the tone of a learning record: what was read, what was understood, what remained unclear.
- Prefer concise, publishable fragments over polished long-form text unless the user asks for a full draft.
- Produce one of these outputs depending on the request:
  - Scrap note: 3-7 bullet points
  - Article fragment: short section with heading and body
  - Final article outline: title, sections, takeaways
- Keep technical claims tied to concrete files and code paths in this repository.
