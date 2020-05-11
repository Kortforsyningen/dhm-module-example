"""DHM Module example plugin."""
import click


@click.command()
@click.argument("infile", type=click.File("rb"))
@click.argument("outfile", type=click.File("wb"))
def inout(infile, outfile):
    """Writes the content of infile to outfile."""
    while True:
        chunk = infile.read(1024)
        if not chunk:
            break
        outfile.write(chunk)
