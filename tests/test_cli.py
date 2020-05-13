import dhm_module_base
from dhm_module_base.cli import cli


def test_cli(cli_runner):
    """Test CLI.

    Args:
        cli_runner (CliRunner): Defined in conftest.py
    """
    result = cli_runner.invoke(cli, ["--version"], catch_exceptions=False)
    assert result.exit_code == 0


def test_cli_version(cli_runner):
    """Test CLI Version.

    Args:
        cli_runner (CliRunner): Defined in conftest.py
    """
    result = cli_runner.invoke(cli, ["--version"], catch_exceptions=False)
    expected = f"dhm_module_base, version {dhm_module_base.__version__}\n"
    assert result.output == expected


def test_cli_plugin_registers(cli_runner):
    """Test that the example was registered into the base module.

    Args:
        cli_runner (CliRunner): Defined in conftest.py
    """
    result = cli_runner.invoke(cli, ["inout", "--help"])
    expected = "Usage: dhm_module_base inout [OPTIONS] [INFILE]... OUTFILE"
    assert result.exit_code == 0
    assert result.output.split("\n")[0] == expected
