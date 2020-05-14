from pathlib import Path
from dhm_module_base.cli import cli


def test_pipe(cli_runner, outfile):
    """Test that the command "pipe" can pipe commands into the inputstream or the outputstream.

    Args:
        cli_runner (CliRunner): Defined in conftest.py
        outfile (temp file): Temporary file defined in conftest.py
    """

    # File is not created yet and does not exist
    assert not outfile.is_file()
    result = cli_runner.invoke(
        cli,
        ["pipe", "--srs", "epsg:25832", "-", str(outfile.resolve())],
        input="\nInput from stdin",  # Mock piping into the instream
    )

    assert result.exit_code == 0
    assert outfile.is_file()
    with open(outfile) as f:
        lines = f.read().splitlines()
        # First line which is the srs output
        assert lines[0] == r'PROJCS["ETRS89 / UTM zone 32N",'
        # Last line which we piped in
        assert lines[-1] == "Input from stdin"
