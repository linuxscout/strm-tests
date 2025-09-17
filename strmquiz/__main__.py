#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main entry point for the STRM test generator.

Usage:
    python -m strm_tests [options]
"""

import logging
import sys
import os
import argparse
import webbrowser
import subprocess
from pathlib import Path


logging.basicConfig(
    level=logging.DEBUG,  # Default log level
    # level=logging.DEBUG,  # Default log level
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        # logging.StreamHandler(sys.stdout),         # Console output
        logging.FileHandler("tmp/logs/quiz.log", encoding="utf-8")  # File output
    ],
)


from strmquiz.quizbuilder import QuizBuilder


class CustomArgumentParser(argparse.ArgumentParser):
    def print_help(self, file=None):
        super().print_help(file)

    def print_help(self, file=None):
        super().print_help(file)
        print("\nExamples of command line usage:\n")
        print("  * Show catalog:")
        print("      python3 -m strmquiz --list\n")
        print("  * Generate test #0 in text format (output to stderr):")
        print("      python3 -m strmquiz -d txt -t test0\n")

        print("  * Generate test #0 in Markdown format (output to stderr):")
        print("      python3 -m strmquiz -d md -t test0\n")

        print("  * Generate test #0 in HTML format (output to a file):")
        print("      python3 -m strmquiz -d html -t test0 -o test.html\n")

        print("  * Read configuration from a file:")
        print("      python3 -m strmquiz -f quiz.conf -d html -t test0 -o test.html\n")

        print("  * Auto-open the output file after generation:")
        print("      python3 -m strmquiz -d html -t test0 -o test.html --preview\n")


def show_catalog():
    """Print formats, categories, and commands."""
    print("\nAvailable formats:")
    for key, desc in QuizBuilder.get_available_formats().items():
        print(f"  - {key:<10} {desc}")

    print("\nAvailable categories:")
    for cat, item in QuizBuilder.get_categories().items():
        print(f"  - {cat:<15} {item['short']}")

    print("\nCommands by category:")
    for cat, item in QuizBuilder.get_categories().items():
        print(f"\n[{cat.capitalize()}]")
        for cmd, info in QuizBuilder.get_commands_info(category=cat).items():
            print(f"   - {cmd:<15} {info['short']}")


def parse_arguments():
    parser = CustomArgumentParser(description="Create Quizzes for STRM 1 - MI.")

    parser.add_argument(
        "-f", "--configfile", help="Input configuration file", metavar="CONFIGFILE"
    )
    parser.add_argument(
        "-g", "--argsfile", help="Input arguments file", metavar="ARGS_FILE"
    )
    parser.add_argument(
        "-o",
        "--outfile",
        required=False,
        help="Output file path",
        metavar="OUTFILE",
        default="",
    )
    parser.add_argument(
        "-d",
        "--outformat",
        help="Output format (text, latex, md)",
        metavar="FORMAT",
        default="text",
    )
    parser.add_argument(
        "-v", "--version", help="Release version", metavar="VERSION", default="0.0.1"
    )
    parser.add_argument(
        "-t",
        "--test_id",
        help="ID of the test to generate (e.g., test1, test2)",
        metavar="TEST_ID",
        default="test1",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        help="Number of test samples to generate",
        metavar="NUMBER",
        default=1,
    )
    parser.add_argument(
        "-c",
        "--category",
        help="Category of tests to generate",
        metavar="CATEGORY",
        default="all",
    )
    parser.add_argument(
        "--min",
        dest="minterms",
        help="Comma-separated list of minterms",
        metavar="MINTERMS",
        default="",
    )
    parser.add_argument(
        "--lang",
        "--language",
        dest="language",
        choices=["ar", "fr", "en", "en-ar","ar-en", "ar-fr"],
        default="arabic",
        help="Language of the test content",
    )

    parser.add_argument(
        "--templates",
        "--templates-dir",
        dest="templates_dir",
        default="",
        help="Set up the templates directory for get question formats",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Open the generated file automatically after creation",
    )
    parser.add_argument(
        "--show-config",
        action="store_true",
        help="Show configuration details for this run",
    )

    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="Show available formats, categories, and commands, then exit.",
    )
    return parser.parse_args()


def preview_file(file_path: str):
    """
    auto-open generated HTML/PDF
    """
    ext = Path(file_path).suffix.lower()
    if ext == ".html":
        webbrowser.open_new_tab(f"file://{os.path.abspath(file_path)}")
    elif ext in (".pdf", ".txt", ".md", ".tex"):
        if sys.platform.startswith("darwin"):  # macOS
            subprocess.run(["open", file_path])
        elif os.name == "nt":  # Windows
            os.startfile(file_path)
        else:  # Linux and others
            subprocess.run(["xdg-open", file_path])


def exit(code=0):
    sys.exit(code)

def main():
    # setup_logging()
    logger = logging.getLogger(__name__)  # module-level logger
    logger.info("Application started")
    logger.debug("Debug message for developers")
    args = parse_arguments()
    if args.list:
        show_catalog()
        exit(0)
    tester = QuizBuilder(
        outformat=args.outformat,
        config_file=args.configfile,
        lang=args.language,
        templates_dir=args.templates_dir,
        args_file=args.argsfile,
    )

    generated_test = tester.get_quiz(args.test_id)
    if args.outfile:
        with open(args.outfile, "w", encoding="utf-8") as output_file:
            output_file.write(generated_test)
        if args.preview:
            preview_file(args.outfile)

    else:
        print(generated_test)
    if args.show_config:
        print(tester.show_config())


if __name__ == "__main__":
    main()
