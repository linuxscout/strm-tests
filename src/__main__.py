#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main entry point for the STRM test generator.

Usage:
    python -m strm_tests [options]
"""

import sys
import argparse
from strm_test import test_builder

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create tests for STRM 1 - MI.')

    parser.add_argument(
        "-f", "--configfile",
        help="Input configuration file",
        metavar="CONFIGFILE"
    )
    parser.add_argument(
        "-o", "--outfile",
        required=True,
        help="Output file path",
        metavar="OUTFILE",
        default="output.txt"
    )
    parser.add_argument(
        "-d", "--outformat",
        help="Output format (text, latex, md)",
        metavar="FORMAT",
        default="text"
    )
    parser.add_argument(
        "-v", "--version",
        help="Release version",
        metavar="VERSION",
        default="0.0.1"
    )
    parser.add_argument(
        "-t", "--test_id",
        help="ID of the test to generate (e.g., test1, test2)",
        metavar="TEST_ID",
        default="test1"
    )
    parser.add_argument(
        "-n", "--number",
        type=int,
        help="Number of test samples to generate",
        metavar="NUMBER",
        default=1
    )
    parser.add_argument(
        "-c", "--category",
        help="Category of tests to generate",
        metavar="CATEGORY",
        default="all"
    )
    parser.add_argument(
        "--min",
        dest="minterms",
        help="Comma-separated list of minterms",
        metavar="MINTERMS",
        default=""
    )

    return parser.parse_args()

def main():
    args = parse_arguments()

    tester = test_builder.test_builder(
        output_format=args.outformat,
        config_file=args.configfile
    )

    generated_test = tester.get_test(args.test_id)

    with open(args.outfile, "w", encoding="utf-8") as output_file:
        output_file.write(generated_test)

if __name__ == '__main__':
    main()
