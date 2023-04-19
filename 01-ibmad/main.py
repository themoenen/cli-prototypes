"""Main"""

import click
from workers.class_extensions import Group
from helpers.welcome_msgs import ibmad_welcome, ds_welcome, gt_welcome, st_welcome, dc_welcome
# from inspect import getmembers
# from pprint import pprint


# https://click.palletsprojects.com/en/8.1.x/api/#decorators
@click.group(cls=Group, invoke_without_command=True)
@click.pass_context
def ibmad(ctx):
    """
    IBM Accelerated Discovery CLI.

    To get an introduction, run <cmd>ibmad</cmd>.
    """
    # pprint(getmembers(ctx))

    if ctx.invoked_subcommand is None:
        click.echo(ibmad_welcome)


@ibmad.command()
def ds():
    """
    IBM Deep Search CLI.

    To get an introduction, run <cmd>ibmad ds</cmd>.
    """
    click.echo(ds_welcome)


@ibmad.command()
def gt():
    """
    IBM Generative Toolkit CLI.

    To get an introduction, run <cmd>ibmad gt</cmd>.
    """
    click.echo(gt_welcome)


@ibmad.command()
def st():
    """
    IBM Simulation Toolkit CLI.

    To get an introduction, run <cmd>ibmad gt</cmd>.
    """
    click.echo(st_welcome)


@ibmad.command()
def dc():
    """
    IBM Digital Chemistry CLI.

    To get an introduction, run <cmd>ibmad gt</cmd>.
    """
    click.echo(dc_welcome)
