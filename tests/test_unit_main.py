import builtins
import logging
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

from strmquiz.quizbuilder import QuizBuilder

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "../", "templates")
import builtins
import sys
import types
from pathlib import Path

import pytest

import strmquiz.__main__ as app  # replace with the actual filename (without .py)
import strmquiz.__main__ as cli  # assuming the file is __main__.py under strm_tests/


def test_parse_arguments_defaults(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog"])  # simulate no args
    args = cli.parse_arguments()
    assert args.outformat == "text"
    assert args.test_id == "test1"
    assert args.language == "arabic"


def test_parse_arguments_list(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "--list"])
    args = cli.parse_arguments()
    assert args.list is True


def test_preview_file_html(monkeypatch):
    called = {}

    def fake_open(url):
        called["url"] = url

    monkeypatch.setattr(cli.webbrowser, "open_new_tab", fake_open)
    cli.preview_file("demo.html")
    assert called["url"].startswith("file://")


def test_preview_file_pdf_linux(monkeypatch):
    called = {}

    def fake_run(cmd, *a, **kw):
        called["cmd"] = cmd

    monkeypatch.setattr(cli, "subprocess", types.SimpleNamespace(run=fake_run))
    monkeypatch.setattr(cli, "os", types.SimpleNamespace(name="posix"))
    monkeypatch.setattr(cli, "sys", types.SimpleNamespace(platform="linux"))

    cli.preview_file("report.pdf")
    assert "xdg-open" in called["cmd"][0]


def test_main_list(monkeypatch):
    # Patch sys.argv so that --list is passed
    monkeypatch.setattr(sys, "argv", ["prog", "--list"])

    # Patch show_catalog so we know it was called
    called = {}
    monkeypatch.setattr(cli, "show_catalog", lambda: called.setdefault("called", True))

    # Patch exit to avoid stopping pytest
    monkeypatch.setattr(
        cli, "exit", lambda code=0: (_ for _ in ()).throw(SystemExit(code))
    )

    with pytest.raises(SystemExit) as e:
        cli.main()

    assert e.value.code == 0
    assert called["called"] is True
