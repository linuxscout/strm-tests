import os
import pytest

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
