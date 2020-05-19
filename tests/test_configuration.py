from pathlib import Path
from dhm_module_base.cli import cli


def test_configuration(cli_runner, data_dir):
    """Test that the command "configuration" can use the inherited configuration object.

    Args:
        cli_runner (CliRunner): Defined in conftest.py
    """
    # Calling the configuration directly without specifying a configuration
    result = cli_runner.invoke(
        cli, ["configuration", "--section", "DEFAULT", "dhm_path"]
    )

    assert result.exit_code == 0
    assert result.output == '"../../tests/data"\n'

    # Calling the base module with a configuration file different from default
    result = cli_runner.invoke(
        cli,
        [
            "-c",
            Path(data_dir) / "config.ini",
            "configuration",
            "--section",
            "DEFAULT",
            "dhm_path",
        ],
    )
    assert result.exit_code == 0
    assert result.output == '"./data"\n'
