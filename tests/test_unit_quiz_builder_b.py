import os
import pytest
import json
import shutil

from strmquiz.quizbuilder import QuizBuilder

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# args_file = PROJECT_ROOT / "args.json"

# TEMPLATES_DIR =os.path.join(PROJECT_ROOT, "templates")


@pytest.fixture
def setup_env(tmp_path):
    """Prepare minimal environment for QuizBuilder to work with real classes."""
    # --- templates dir (must exist)
    templates_dir = PROJECT_ROOT / "templates"
    # templates_dir.mkdir()
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    shutil.copy(
        PROJECT_ROOT / "strmquiz" / "config" / "args.default.json",
        tmp_path / "config" / "args.default.json",
    )

    # --- config file (must exist, even minimal content)
    config_file = tmp_path / "quiz.test2.conf"
    # config_file.name()
    # --- args file: schema with at least one command & arg
    args_file = tmp_path / "args.test.json"
    config_file.write_text(
        f"""[DEFAULT]\ndummy=1\ntemplates_dir="templates"\nargs_file="{args_file}" """
    )

    # --- args file: schema with at least one command & arg
    args_data = {
        "float": {"float": 42},  # Example: float command with one int arg
    }
    args_file.write_text(json.dumps(args_data))
    assert args_file.exists()

    return str(templates_dir), str(config_file), str(args_file)


@pytest.fixture
def builder(setup_env):
    templates_dir, config_path, args_file = setup_env
    # You may need to pass a templates_dir if question_builder expects it
    return QuizBuilder(
        outformat="latex",
        config_file=config_path,
        lang="en",
        templates_dir=templates_dir,
    )


def test_load_args_from_file(setup_env):
    templates_dir, config_file, args_file = setup_env

    qb = QuizBuilder(
        outformat="html",
        config_file=config_file,
        lang="en",
        templates_dir=templates_dir,
        args_file=args_file,
    )

    result = qb.my_args_dict  # already loaded in __init__
    assert isinstance(result, dict)
    assert "float" in result
    assert "float" in result["float"]  # should validate arg "float"
    assert result["float"]["float"] == 42.0


# @pytest.mark.skip(reason="later")
def test_load_args_from_dict(setup_env):
    templates_dir, config_file, args_file = setup_env

    qb = QuizBuilder(
        outformat="html",
        config_file=config_file,
        lang="en",
        templates_dir=templates_dir,
        args_file=args_file,
    )

    # Provide args directly instead of file
    args_src = {
        "float": {"float": 99},
    }
    result = qb.load_args(args_src)

    assert "float" in result
    assert result["float"]["float"] == 99


@pytest.mark.skip(reason="later")
def test_load_args_empty_source(setup_env):
    templates_dir, config_file, args_file = setup_env

    qb = QuizBuilder(
        outformat="html",
        config_file=config_file,
        lang="en",
        templates_dir=templates_dir,
        args_file=args_file,
    )

    # Force case: empty source and args_file = None
    qb.args_file = ""
    result = qb.load_args({})
    assert result == {}


def test_load_args_uses_default_file(
    setup_env,
    tmp_path,
    monkeypatch,
):
    """If args_file is not passed, QuizBuilder should load the default args file."""
    # --- templates dir
    templates_dir, config_file, _ = setup_env

    # Patch __file__ so QuizBuilder resolves default args path inside tmp_path
    monkeypatch.setattr(
        "strmquiz.quizbuilder.__file__", str(tmp_path / "quizbuilder.py")
    )

    qb = QuizBuilder(
        outformat="html",
        config_file=config_file,
        lang="en",
        templates_dir=templates_dir,
        args_file="",  # force empty
    )

    result = qb.my_args_dict
    assert "float" in result
    assert result["float"]["float"] == 42
