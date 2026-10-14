#!/usr/bin/env python3
"""Summarize a `claude plugin eval` run.

Prints one line per case and, for failed graders, the agent's final answer
so you can see why it failed without opening the HTML report.

Usage: python3 scripts/eval_summary.py [aggregate-result.json] [--markdown]
Defaults to the newest evals/results/*/aggregate-result.json.
--markdown prints a results table for evals/RESULTS.md instead.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def newest_result():
    runs = sorted((ROOT / "evals" / "results").glob("*/aggregate-result.json"))
    if not runs:
        sys.exit("no eval results found under evals/results/")
    return runs[-1]


def rows(data):
    for case in data["cases"]:
        for arm, runs in case["arms"].items():
            for run in runs:
                yield case["name"], arm, run


def count(data):
    """(passed, total) over runs, independent of the --threshold used for the run."""
    results = [run["passed"] for _, arm, run in rows(data) if arm == "with"]
    return sum(results), len(results)


def print_details(data):
    for name, arm, run in rows(data):
        mark = "PASS" if run["passed"] else "FAIL"
        print(f"{mark} {run['score']:.2f}  {name} [{arm}]  ${run['costUsd']:.2f}")
        if run.get("error"):
            print(f"     error: {run['error']}")
        failed = [g for g in run["graders"] if g.get("scored", True) and not g["passed"]]
        for g in failed:
            print(f"     ✗ {g['name']}: {g['explanation']}")
        if failed and failed[0].get("evidence"):
            print("     --- final answer ---")
            print("     " + failed[0]["evidence"].replace("\n", "\n     "))
    passed, total = count(data)
    print(f"\n{passed}/{total} runs passed every grader · "
          f"mean score {data['aggregates']['overallScore']:.2f} · ${data['costUsd']:.2f}")


def print_markdown(data):
    date = data["startedAt"][:10]
    print("| Date | Case | Score | Passed | Failed graders |")
    print("| --- | --- | --- | --- | --- |")
    for name, arm, run in rows(data):
        if arm != "with":
            continue
        failed = ", ".join(g["name"] for g in run["graders"] if g.get("scored", True) and not g["passed"])
        print(f"| {date} | `{name}` | {run['score']:.2f} | {'✅' if run['passed'] else '❌'} | {failed or '—'} |")


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    path = Path(args[0]) if args else newest_result()
    data = json.loads(path.read_text(encoding="utf-8"))
    if "--markdown" in argv:
        print_markdown(data)
    else:
        print_details(data)
    passed, total = count(data)
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
