#!/usr/bin/env python3
"""Normalize readable or YouTube rolling VTT captions into a TSV cue table."""

from __future__ import annotations

import argparse
import html
import re
from dataclasses import dataclass
from pathlib import Path


TIMING = re.compile(r"^(\d{2}:\d{2}:\d{2}\.\d{3})\s+-->\s+(\d{2}:\d{2}:\d{2}\.\d{3})")
TAG = re.compile(r"<[^>]+>")
SPACE = re.compile(r"\s+")


@dataclass
class Cue:
    start: str
    end: str
    text: str


def clean_text(value: str) -> str:
    return SPACE.sub(" ", html.unescape(TAG.sub("", value))).strip()


def parse_vtt(path: Path) -> tuple[list[Cue], bool]:
    source = path.read_text(encoding="utf-8-sig")
    rolling = "<c>" in source or bool(re.search(r"<\d{2}:\d{2}:\d{2}\.\d{3}>", source))
    cues: list[Cue] = []
    # Empty-space lines inside a YouTube cue must not terminate its payload.
    for block in re.split(r"\n\n+", source.replace("\r\n", "\n")):
        lines = block.splitlines()
        for i, line in enumerate(lines):
            match = TIMING.match(line)
            if not match:
                continue
            payload = [x.strip() for x in lines[i+1:] if x.strip()]
            if payload:
                text = clean_text(payload[-1] if rolling else " ".join(payload))
                if text:
                    cues.append(Cue(*match.groups(), text))
            break
    return cues, rolling


def deduplicate(cues: list[Cue], rolling: bool) -> list[Cue]:
    result: list[Cue] = []
    for cue in cues:
        if not result:
            result.append(cue)
            continue
        previous = result[-1]
        if cue.text == previous.text or previous.text.startswith(cue.text):
            previous.end = cue.end
            continue
        if rolling and cue.text.startswith(previous.text):
            previous.text = cue.text
            previous.end = cue.end
            continue
        result.append(cue)
    return result


def write_tsv(path: Path, cues: list[Cue]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = ["start\tend\ttext"]
    rows.extend(f"{cue.start}\t{cue.end}\t{cue.text}" for cue in cues)
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input .vtt file")
    parser.add_argument("output", type=Path, help="Output .tsv file")
    args = parser.parse_args()

    cues, rolling = parse_vtt(args.input)
    cleaned = deduplicate(cues, rolling)
    write_tsv(args.output, cleaned)
    reduction = 0 if not cues else (1 - len(cleaned) / len(cues)) * 100
    print(
        f"input={args.input.name} mode={'rolling' if rolling else 'readable'} "
        f"parsed={len(cues)} cleaned={len(cleaned)} reduction={reduction:.1f}% output={args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
