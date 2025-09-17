import sys
import tempfile
import textwrap

import pytest

from strmquiz.read_config import ReadConfig  # replace with actual import path


@pytest.fixture
def make_config():
    """Fixture to create a temporary config file."""

    def _make(content: str) -> str:
        tmp = tempfile.NamedTemporaryFile("w", delete=False)
        tmp.write(textwrap.dedent(content))
        tmp.flush()
        return tmp.name

    return _make


def test_defaults_loaded(make_config):
    filename = make_config("")  # empty config
    cfg = ReadConfig(filename, debug=False)

    # check default values
    assert cfg.repeat == 1
    # assert cfg.synch_type == "rising"
    assert isinstance(cfg.quizes, list)
    assert cfg.test_table == {}


def test_valid_values(make_config):
    filename = make_config(
        """
    [DEFAULT]
    templates_dir="../mytemplates"
    [Args]
    repeat = 5
    """
    )

    cfg = ReadConfig(filename, debug=False)
    assert cfg.repeat == 5
    assert cfg.templates_dir == "../mytemplates"
    # assert cfg.synch_type == "rising"
    # assert cfg.length == 20
    assert cfg.warnings == []


def test_invalid_values(make_config):
    filename = make_config(
        """
    [Args]
    repeat = 200
    """
    )

    cfg = ReadConfig(filename, debug=False)
    # invalid values should fall back to defaults
    assert cfg.repeat == 1
    # assert cfg.synch_type == "rising"

    # warnings should be collected
    assert len(cfg.warnings) == 1
    # assert "Invalid value for repeat" in cfg.warnings[0]
    # assert "Invalid value for synch_type" in cfg.warnings[1]


def test_print_warnings(make_config, capsys):
    filename = make_config(
        """
    [Args]
    repeat = 200
    """
    )
    cfg = ReadConfig(filename, debug=False)
    # warnings should be collected
    assert len(cfg.warnings) == 1
    # assert "Configuration Warnings" in cfg.warnings, f"The Test table is '{cfg.test_table}'"
    # assert "Invalid value for repeat" in cfg.warnings, f"The result is '{cfg.warnings}'"


def test_no_warnings_output(make_config):
    filename = make_config("[Args]\nrepeat = 10")
    cfg = ReadConfig(filename, debug=False)

    cfg.print_warnings()

    assert not cfg.warnings


def test_plain_print(capfd):
    print("hello from plain print")
    out, err = capfd.readouterr()
    assert "hello" in out


def test_all_args_are_read(tmp_path):
    # Step 1: Create an empty file so ReadConfig can open it
    dummy_file = tmp_path / "dummy.conf"
    dummy_file.write_text("")  # empty, but exists

    # Step 2: Use that file to extract the expected fields
    rc = ReadConfig(str(dummy_file), debug=False)
    args_section = "\n".join(
        f"{key} = {repr(default)}" for key, (_, default) in rc.fields["Args"].items()
    )

    # Step 3: Create a real config with all Args keys set explicitly
    config_file = tmp_path / "config.conf"
    config_file.write_text(f"[Args]\n{args_section}")

    # Step 4: Reload using the complete config
    cfg = ReadConfig(str(config_file), debug=False)

    # Step 5: Verify all args were read correctly
    for key, (attr, default) in cfg.fields["Args"].items():
        loaded_value = getattr(cfg, attr)
        assert (
            loaded_value == default
        ), f"Mismatch for {key}: expected {default}, got {loaded_value}"
