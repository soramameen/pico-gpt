#!/usr/bin/env python3
"""
Build a Japanese conversation corpus from an open Hugging Face dataset and
write it to datasets/japanese_conversation_training.txt in "Human:/Assistant:" format.

Current source:
  - shi3z/Japanese_wikipedia_conversation_100K (license: MIT)

Usage:
  python scripts/build_japanese_conversation_corpus.py [--max_rows N]
"""

import argparse
import os
from typing import Iterable, List, Tuple

from datasets import load_dataset

DATASET_ID = "shi3z/Japanese_wikipedia_conversation_100K"
OUTPUT_PATH = os.path.join("datasets", "japanese_conversation_training.txt")


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def extract_pairs_from_messages(messages) -> List[Tuple[str, str]]:
    pairs: List[Tuple[str, str]] = []
    pending_user: str | None = None
    for msg in messages or []:
        role = (msg.get("role") or msg.get("from") or "").lower()
        text = (msg.get("content") or msg.get("value") or msg.get("text") or "").strip()
        if not text:
            continue
        if role in ("user", "human"):
            pending_user = text
        elif role in ("assistant", "gpt") and pending_user:
            pairs.append((pending_user, text))
            pending_user = None
    return pairs


def normalize_text(text: str) -> str:
    return " ".join((text or "").split())


def write_pairs(f, pairs: Iterable[Tuple[str, str]]) -> int:
    written = 0
    for user_text, assistant_text in pairs:
        user_text = normalize_text(user_text)
        assistant_text = normalize_text(assistant_text)
        if not user_text or not assistant_text:
            continue
        f.write(f"Human: {user_text}\nAssistant: {assistant_text}\n\n")
        written += 1
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description="Build Japanese conversation corpus")
    parser.add_argument("--max_rows", type=int, default=None, help="Limit source rows for quick runs")
    args = parser.parse_args()

    ensure_dir("datasets")
    split = "train"
    if args.max_rows:
        split = f"train[:{args.max_rows}]"

    print(f"Loading dataset: {DATASET_ID} ({split})")
    ds = load_dataset(DATASET_ID, split=split)

    total_rows = 0
    total_pairs = 0
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for row in ds:
            total_rows += 1
            pairs = extract_pairs_from_messages(row.get("conversations") or row.get("messages") or [])
            total_pairs += write_pairs(f, pairs)

    print(f"Wrote corpus to: {OUTPUT_PATH}")
    print(f"Rows processed: {total_rows}")
    print(f"Pairs written: {total_pairs}")


if __name__ == "__main__":
    main()
