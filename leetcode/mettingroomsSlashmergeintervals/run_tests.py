#!/usr/bin/env python3
"""
Local test runner for Meeting Rooms / Merge Intervals.

Usage:
    python run_tests.py           # run all tests
    python run_tests.py -v        # verbose (show passing cases too)
    python run_tests.py -k ex1    # run cases whose name contains "ex1"
"""

import argparse
import sys
import time
import traceback
from dataclasses import dataclass
from typing import List, Optional

from solution import min_desks


@dataclass
class TestCase:
    name: str
    trades: List[List[int]]
    expected: int


TEST_CASES: List[TestCase] = [
    TestCase("example 1", [[0, 30], [5, 10], [15, 25]], 2),
    TestCase("example 2", [[0, 10], [10, 20], [20, 30]], 1),
    TestCase("empty", [], 0),
    TestCase("single trade", [[0, 10]], 1),
    TestCase("all overlap", [[0, 10], [1, 9], [2, 8], [3, 7]], 4),
    TestCase("nested intervals", [[0, 100], [10, 20], [15, 25], [30, 40]], 2),
    TestCase("disjoint pairs", [[0, 5], [6, 10], [11, 15], [16, 20]], 1),
    TestCase("touching endpoints", [[0, 5], [5, 10], [0, 10]], 2),
    TestCase("same start different end", [[0, 5], [0, 10], [0, 15]], 3),
    TestCase("unsorted input", [[15, 25], [0, 30], [5, 10]], 2),
]


def run_case(case: TestCase) -> tuple[bool, str, Optional[float]]:
    try:
        start = time.perf_counter()
        actual = min_desks(case.trades)
        elapsed_ms = (time.perf_counter() - start) * 1000
    except Exception:
        return False, traceback.format_exc().rstrip(), None

    if actual == case.expected:
        return True, f"got {actual}", elapsed_ms

    return (
        False,
        f"got {actual}, expected {case.expected}",
        elapsed_ms,
    )


def format_trades(trades: List[List[int]]) -> str:
    return str(trades)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Meeting Rooms test cases")
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="print passing cases",
    )
    parser.add_argument(
        "-k",
        "--keyword",
        default="",
        help="only run cases whose name contains this substring (case-insensitive)",
    )
    args = parser.parse_args()

    keyword = args.keyword.lower()
    cases = [c for c in TEST_CASES if keyword in c.name.lower()] if keyword else TEST_CASES

    if not cases:
        print(f"No test cases match keyword: {args.keyword!r}")
        return 1

    passed = 0
    failed = 0

    print(f"Running {len(cases)} test case(s)\n")

    for i, case in enumerate(cases, start=1):
        ok, detail, elapsed_ms = run_case(case)
        status = "PASS" if ok else "FAIL"

        if ok:
            passed += 1
            if args.verbose:
                timing = f" ({elapsed_ms:.2f}ms)" if elapsed_ms is not None else ""
                print(f"[{status}] {i:02d}. {case.name}{timing}")
                print(f"       input:    {format_trades(case.trades)}")
                print(f"       expected: {case.expected}")
                print(f"       {detail}\n")
        else:
            failed += 1
            timing = f" ({elapsed_ms:.2f}ms)" if elapsed_ms is not None else ""
            print(f"[{status}] {i:02d}. {case.name}{timing}")
            print(f"       input:    {format_trades(case.trades)}")
            print(f"       expected: {case.expected}")
            print(f"       {detail}\n")

    print(f"Results: {passed} passed, {failed} failed, {len(cases)} total")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
