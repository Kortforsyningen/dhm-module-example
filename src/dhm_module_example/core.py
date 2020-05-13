"""DHM Module example plugin."""
import logging
import click


# Logger inherits color options from base_module
logger = logging.getLogger(__name__)


@click.command()
@click.argument("infile", type=click.File("rb"), nargs=-1)
@click.argument("outfile", type=click.File("wb"))
def inout(infile, outfile):
    """Example command inout.

    Writes the contents of infile to outfile. If outfile does not exist it is created,
    if it exists it is overwritten only if --overwrite is set explicitly to true.
    """
    # Returns True for files and directories
    for f in infile:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            outfile.write(chunk)
            outfile.flush()
