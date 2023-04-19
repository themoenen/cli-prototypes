import click


@click.group(invoke_without_command=True)
@click.pass_context
def ibmad(ctx):
    """
    IBM Accelerated Discovery CLI.
    ------------------------------

    Your commands:

    ibmad
    ibmad --help
    ibmad gt
    ibmad ds
    ibmad st
    ibmad dc
    ibmad gt --help
    ibmad ds --help
    ibmad st --help
    ibmad dc --help

    """
    # pprint(getmembers(ctx))

    if ctx.invoked_subcommand is None:
        click.echo(ibmad.__doc__)


@ibmad.command()
def ds():
    """
    IBM Deep Search CLI.
    """
    click.echo(ds.__doc__)


@ibmad.command()
def gt():
    """
    IBM Generative Toolkit CLI.
    """
    click.echo(gt.__doc__)


@ibmad.command()
def st():
    """
    IBM Simulation Toolkit CLI.
    """
    click.echo(st.__doc__)


@ibmad.command()
def dc():
    """
    IBM Digital Chemistry CLI.
    """
    click.echo(dc.__doc__)
