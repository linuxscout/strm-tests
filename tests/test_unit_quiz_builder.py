import json
import os
import shutil
from pathlib import Path

import pytest

from strmquiz.quizbuilder import QuizBuilder

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# args_file = PROJECT_ROOT / "args.json"

TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "templates")


@pytest.fixture
def config_path(tmp_path):
    """Create a minimal config file for integration testing."""
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    shutil.copy(
        PROJECT_ROOT / "strmquiz" / "config" / "args.default.json",
        tmp_path / "args.test.json",
    )

    cfg_file = tmp_path / "config" / "quiz.test.conf"
    cfg_file.write_text(
        """
[Default]
templates_dir="templates"
args_file="args.test.json"
[QUIZES]
quizes = ["test0", "test1", "test2", "test3", "test4", "test5","test6", "test7","bankquestion", "test8", "test9"]
commands =["float", 
 "intervalle",
 "complement",
 "exp",            
 "map",
 "map-sop",
 "function",
 "base",
 "arithm",
 "mesure",
 "static_funct",
 "multi_funct"]
[Tests]
test0=[["counter"]]
test1=[["base", "intervalle", "arithm"],
 ["mesure", "base", "arithm"],
 ["base", "mesures", "arithm"],]
        """,
        encoding="utf-8",
    )

    templates_dir = TEMPLATES_DIR
    args_file = tmp_path / "args.test.json"
    return str(templates_dir), str(cfg_file), str(args_file)


@pytest.fixture
def builder(config_path):
    templates_dir, config_path, args_file = config_path
    # You may need to pass a templates_dir if question_builder expects it
    return QuizBuilder(
        outformat="latex",
        config_file=config_path,
        args_file=args_file,
        lang="en",
        templates_dir=templates_dir,
    )


def test_list_commands_real(builder):
    cmds = builder.list_commands()
    assert "float" in cmds
    assert "function" in cmds


def test_get_question_real(builder):
    """Call some real question types without mocking."""
    qtext, ans = builder.get_question("float")
    assert isinstance(qtext, str)


def test_build_quiz_real(builder):
    """Build a quiz with real questions."""
    builder.build_quiz(["float", "function"], rand=False, nb=2)
    # The formatter inside builder should now have something
    output = builder.formater.display()
    assert isinstance(output, str)
    assert "Q1" in output or "Q2" in output


def test_get_quiz_from_config(builder):
    """Run a quiz generation based on test config file."""
    output = builder.get_quiz("test1")
    assert isinstance(output, str)
    assert "Question" in output or "Q1" in output


# ---------------------- TESTS ----------------------


def test_list_commands_real(builder):
    cmds = builder.get_commands_list()
    assert "float" in cmds
    assert "function" in cmds
    assert isinstance(cmds, list)


# @pytest.mark.skip(reason="To be removed manually")
def test_get_commands_list_all(builder):
    cmds = builder.get_commands_list()
    assert isinstance(cmds, list)
    assert "float" in cmds
    assert "chronogram" in cmds


# @pytest.mark.skip(reason="To be removed manually")
def test_get_commands_list_by_category(builder):
    cmds = builder.get_commands_list("boolean algebra")
    assert "function" in cmds
    assert "map" in cmds
    assert "float" not in cmds


# @pytest.mark.skip(reason="To be removed manually")
def test_get_commands_info_all(builder):
    info = builder.get_commands_info()
    assert "float" in info
    assert isinstance(info["float"], dict)


# @pytest.mark.skip(reason="To be removed manually")
def test_get_commands_info_by_category(builder):
    info = builder.get_commands_info(category="encoding")
    assert "float" in info, f"The result is {info}"


# @pytest.mark.skip(reason="To be removed manually")
def test_get_categories(builder):
    cats = builder.get_categories()
    assert "boolean algebra" in cats, f"Categories {cats}"
    assert "encoding" in cats
    assert isinstance(cats["boolean algebra"]["commands"], list)
    assert any(cmd["name"] == "map" for cmd in cats["boolean algebra"]["commands"])


# @pytest.mark.skip(reason="To be removed manually")
def test_get_short_description(builder):
    desc = builder.get_short_description("float")
    assert "Float" in desc
    desc_unknown = builder.get_short_description("unknown")
    assert "No short description" in desc_unknown


# @pytest.mark.skip(reason="To be removed manually")
def test_get_long_description(builder):
    desc = builder.get_long_description("function")
    assert "Boolean function" in desc
    desc_unknown = builder.get_long_description("unknown")
    assert "No long description" in desc_unknown


# @pytest.mark.skip(reason="To be removed manually")
def test_get_random_commands(builder):
    cmds = builder.get_random_commands(n=2)
    assert isinstance(cmds, dict)
    assert len(cmds) <= 2
    for cmd in cmds:
        assert cmd in builder.commands_info


# @pytest.mark.skip(reason="To be removed manually")
def test_get_random_commands_list(builder):
    cmds = builder.get_random_commands_list(n=2)
    assert isinstance(cmds, list)
    assert len(cmds) <= 2
    for cmd in cmds:
        assert cmd in builder.commands_info


# @pytest.mark.skip(reason="Manual run: test all commands against quiz_builder.get_question()")
def test_all_commands_generate_questions(builder):
    """
    Iterate over all commands in quiz_builder and check
    that get_question() runs without errors.
    """
    commands = builder.get_commands_list()
    assert commands, "No commands available in quiz_builder."

    for cmd in commands:
        try:
            question, answer = builder.get_question(command=cmd)
            assert question is not None, f"Question is None for command {cmd}"
            assert answer is not None, f"Answer is None for command {cmd}"
        except Exception as e:
            pytest.fail(f"Command '{cmd}' raised an exception: {e}")


def test_load_categories(builder):
    cats = builder.categories_info
    assert isinstance(cats, dict), f"Categories : {cats}"


def test_load_commands(builder):
    cmds = builder.commands_info
    assert isinstance(cmds, dict), f"Commands : {cmds}"
