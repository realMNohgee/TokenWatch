#!/usr/bin/env python3
"""
TokenWatch — real-time context window monitor for AI agents.

Track token usage during an agent session. Warn at configurable thresholds
(75% default). Suggest what to summarize or truncate when context is filling up.
Uses word-count heuristic (adjustable token-per-word factor).

Pure Python standard library. Zero dependencies.

Domains: agent optimization · context management · cost control.
"""
import argparse, json, sys

TPW = 1.3  # avg tokens per English word


def count(text):
    return int(len(text.split()) * TPW)


def cmd(args):
    text = open(args.input, encoding="utf-8").read() if args.input else sys.stdin.read()
    total = count(text)
    pct = round(total / args.limit * 100, 1) if args.limit else 0
    out = {"total": total, "limit": args.limit, "pct": pct}
    if pct >= args.warn:
        out["warn"] = f"{pct}% of context used"
        segs = sorted(
            [{"tokens": count(p), "preview": p.split("\n")[0][:80]}
             for p in text.split("\n\n") if p.strip()],
            key=lambda s: s["tokens"], reverse=True
        )[:3]
        out["trim"] = segs
    if args.format == "json":
        print(json.dumps(out, indent=2))
    else:
        bar = "\u2588" * int(pct / 5) + "\u2591" * (20 - int(pct / 5))
        print(f"[{bar}] {pct}%  ({total}/{args.limit})")
        for c in out.get("trim", []):
            print(f"  {c['tokens']} tok: {c['preview']}")
    return 1 if "warn" in out else 0


def main():
    p = argparse.ArgumentParser(prog="tokenwatch", description=__doc__)
    p.add_argument("--input", help="text file (or stdin)")
    p.add_argument("--limit", type=int, default=128000)
    p.add_argument("--warn", type=float, default=75)
    p.add_argument("--format", choices=["text", "json"], default="text")
    p.set_defaults(func=cmd)
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
