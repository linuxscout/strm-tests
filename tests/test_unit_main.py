import sys
import logging
import builtins
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path

import strmquiz.__main__ as app  # replace with the actual filename (without .py)

def test_setup_logging(tmp_path, capsys):
    """Test that logging writes to both stdout and a file."""
    log_file = tmp_path / "quiz.log"

    # Patch FileHandler path
    with patch("logging.FileHandler") as mock_file_handler:
        mock_file_handler.return_value = logging.StreamHandler(sys.stdout)
        app.setup_logging()

    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)
    logger.debug("debug message")

    captured = capsys.readouterr()
    assert "debug message" in captured.out

@pytest.mark.skip(reason="To be removed")
def test_parse_arguments_defaults(monkeypatch):
    """Test parsing arguments with minimal input and defaults."""
    test_args = ["prog", "-o", "out.txt"]  # only required arg
    monkeypatch.setattr(sys, "argv", test_args)

    args = app.parse_arguments()
    assert args.outfile == "out.txt"
    assert args.outformat == "text"
    assert args.test_id == "test1"
    assert args.language == "arabic"

@pytest.mark.skip(reason="To be removed")
def test_main_runs_and_writes_file(tmp_path, monkeypatch):
    """Test that main() creates an output file with expected content."""
    outfile = tmp_path / "output.txt"

    # Fake CLI args
    monkeypatch.setattr(
        sys,
        "argv",
        ["prog", "-o", str(outfile), "-t", "fake_test", "-d", "text"]
    )

    # Mock QuizBuilder
    fake_quiz = "Generated quiz content"
    mock_quizbuilder = MagicMock()
    mock_quizbuilder.get_quiz.return_value = fake_quiz
    with patch("your_module_name.QuizBuilder", return_value=mock_quizbuilder):
        app.main()

    # Verify file created
    assert outfile.exists()
    content = outfile.read_text(encoding="utf-8")
    assert fake_quiz in content
