# pylint: disable=redefined-outer-name
from pathlib import Path
import pytest
from click.testing import CliRunner


@pytest.fixture(scope="function")
def cli_runner():
    return CliRunner()


@pytest.fixture(scope="session")
def data_dir():
    """Absolute file path to the dir with test data."""
    return Path("./tests/data").absolute().resolve()


@pytest.fixture(scope="session")
def infile(data_dir):
    return Path(data_dir) / "infile.txt"


@pytest.fixture(scope="function")
def outfile(tmpdir):
    return Path(tmpdir.join("outfile.txt"))
