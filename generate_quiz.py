#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate tests for Structure Machine course (STRM 1 - MI).
Author: Taha Zerrouki <zerrouki@majd4>
License: GPL v2 or later
"""

import argparse
from strmquiz.quizbuilder import QuizBuilder


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create tests for STRM 1 (Math & Informatics).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-f", dest="configfile", metavar="CONFIGFILE",
        help="Input configuration file"
    )
    parser.add_argument(
        "-o", dest="outfile", metavar="OUTFILE", required=True,
        help="Output file for the generated test"
    )
    parser.add_argument(
        "-d", dest="outformat", metavar="FORMAT", default="text",
        help="Output format (text, latex, md, json)"
    )
    parser.add_argument(
        "-v", dest="version", metavar="VERSION", default="0.0.1",
        help="Release version"
    )
    parser.add_argument(
        "-t", dest="test_id", metavar="TEST_ID", type=str, default="1",
        help="Test ID to generate (e.g., test1, test2, ...)"
    )
    parser.add_argument(
        "-n", dest="number", metavar="NUMBER", type=int, default=1,
        help="Number of samples to generate"
    )
    parser.add_argument(
        "-c", dest="category", metavar="CATEGORY", type=str, default="all",
        help="Category of test questions"
    )
    parser.add_argument(
        "--min", dest="minterms", metavar="MINTERMS", type=str, default="",
        help="Comma-separated list of minterms (if applicable)"
    )
    return parser.parse_args()


def generate_test(args):
    tester = QuizBuilder(args.outformat, config_file=args.configfile)
    return tester.get_quiz(args.test_id)


def main():
    args = parse_args()
    content = generate_test(args)

    try:
        with open(args.outfile, "w", encoding="utf8") as f:
            f.write(content)
        # print(f"Test written to {args.outfile}")
    except IOError as e:
        print(f"Error writing to {args.outfile}: {e}")
        return 1
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
