from pathlib import Path
from dhm_module_base.cli import cli


def test_inout(cli_runner, infile, outfile):
    """Test that the command "inout" copies the infile to the output.

    Args:
        cli_runner (CliRunner): Defined in conftest.py
    """
    # File is not created yet and does not exist
    assert not outfile.is_file()

    result = cli_runner.invoke(
        cli, ["inout", str(infile.resolve()), str(outfile.resolve())]
    )

    assert result.exit_code == 0
    assert outfile.is_file()
    # Compare file size
    assert infile.stat().st_size == outfile.stat().st_size
