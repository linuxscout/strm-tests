import os
import pytest
import json

from strmquiz.quizbuilder import QuizBuilder
TEMPLATES_DIR =os.path.join(os.path.dirname(__file__), "../","templates")


@pytest.fixture
def config_path(tmp_path):
    """Create a minimal config file for integration testing."""
    cfg_file = tmp_path / "quiz6.conf"
    cfg_file.write_text(
        """
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
        encoding="utf-8"
    )
    return str(cfg_file)


@pytest.fixture
def builder(config_path):
    # You may need to pass a templates_dir if question_builder expects it
    return QuizBuilder(outformat="latex", config_file=config_path, lang="en", templates_dir=TEMPLATES_DIR)


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


@pytest.fixture
def setup_env(tmp_path):
    """Prepare minimal environment for QuizBuilder to work with real classes."""
    # --- templates dir (must exist)
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()

    # --- config file (must exist, even minimal content)
    config_file = tmp_path / "quiz.conf"
    config_file.write_text("[DEFAULT]\ndummy=1\n")

    # --- args file: schema with at least one command & arg
    args_file = tmp_path / "args.json"
    args_data = {
        "float": {"float": 42},   # Example: float command with one int arg
    }
    args_file.write_text(json.dumps(args_data))

    return str(templates_dir), str(config_file), str(args_file)


def test_load_args_from_file(setup_env):
    templates_dir, config_file, args_file = setup_env

    qb = QuizBuilder(
        outformat="html",
        config_file=config_file,
        lang="en",
        templates_dir=templates_dir,
        args_file=args_file,
    )

    result = qb.my_args_dict   # already loaded in __init__
    assert isinstance(result, dict)
    assert "float" in result
    assert "float" in result["float"]   # should validate arg "float"
    assert result["float"]["float"] == 42

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

def test_load_args_uses_default_file(tmp_path, monkeypatch,):
    """If args_file is not passed, QuizBuilder should load the default args file."""
    # --- templates dir
    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()

    # --- config file
    config_file = tmp_path / "quiz.conf"
    config_file.write_text("[DEFAULT]\ndummy=1\n")

    # --- fake default args file path inside quizbuilder/config
    default_config_dir = tmp_path / "config"
    default_config_dir.mkdir()
    default_args_file = default_config_dir / "args.default.json"
    default_args_file.write_text('{"float": {"float": 7}}')

    # Patch __file__ so QuizBuilder resolves default args path inside tmp_path
    monkeypatch.setattr("strmquiz.quizbuilder.__file__", str(tmp_path / "quizbuilder.py"))

    qb = QuizBuilder(
        outformat="html",
        config_file=config_file,
        lang="en",
        templates_dir=templates_dir,
        args_file="",   # force empty
    )

    result = qb.my_args_dict
    assert "float" in result
    assert result["float"]["float"] == 7

def test_load_categories(builder):
    cats = builder.categories_info
    assert isinstance(cats, dict), f"Categories : {cats}"

def test_load_commands(builder):
    cmds = builder.commands_info
    assert isinstance(cmds, dict), f"Commands : {cmds}"