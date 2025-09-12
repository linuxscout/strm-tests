#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main entry point for the STRM test generator.

Usage:
    python -m strm_tests [options]
"""

import logging
import sys
import argparse

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,  # Default log level
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),         # Console output
            logging.FileHandler("tmp/logs/quiz.log", encoding="utf-8")  # File output
        ]
    )

logger = logging.getLogger(__name__)


from strmquiz.quizbuilder import QuizBuilder

class CustomArgumentParser(argparse.ArgumentParser):
    def print_help(self, file=None):
        super().print_help(file)
        qz = QuizBuilder(config_file="", templates_dir=".")
        # Custom message before the help
        print("Custom Help Message:")
        print("Available formats are:")
        for k, v in QuizBuilder.get_available_formats().items():
            print(f"\t{k}:\t{v}")
        print("Available Categories are:")
        for c, item in qz.get_categories().items():
            print(f"\t{c}:\t{item['short']}")

        for c in qz.get_categories():
            print(f"{c.capitalize()} category: available Commands:")
            for cmd, item in qz.get_commands_info(category=c).items():
                print(f"\t{cmd}:\t{item['short']}")


def parse_arguments():
    parser = CustomArgumentParser(description='Create Quizzes for STRM 1 - MI.')

    parser.add_argument(
        "-f", "--configfile",
        help="Input configuration file",
        metavar="CONFIGFILE"
    )
    parser.add_argument(
        "-g", "--argsfile",
        help="Input arguments file",
        metavar="ARGS_FILE"
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
    parser.add_argument(
        "--lang", "--language",
        dest="language",
        choices=["ar", "fr", "en", "ar-en", "ar-fr"],
        default="arabic",
        help="Language of the test content"

    )

    parser.add_argument(
        "--templates", "--templates-dir",
        dest="templates_dir",
        default="",
        help="Set up the templates directory for get question formats"
    )

    return parser.parse_args()

def main():
    setup_logging()
    logger = logging.getLogger(__name__)  # module-level logger
    logger.info("Application started")
    logger.debug("Debug message for developers")
    args = parse_arguments()

    tester = QuizBuilder(
        outformat=args.outformat,
        config_file=args.configfile,
        lang = args.language,
        templates_dir=args.templates_dir,
        args_file=args.argsfile,
    )

    generated_test = tester.get_quiz(args.test_id)

    with open(args.outfile, "w", encoding="utf-8") as output_file:
        output_file.write(generated_test)

if __name__ == '__main__':
    main()
