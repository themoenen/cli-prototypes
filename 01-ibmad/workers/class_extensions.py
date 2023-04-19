"""Extensions of some built-in click classes."""

import click
from .help_formatter import HelpFormatter


class Group(click.Group):
    """Extends the click.Group commands with a custom formatter."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all subcommands use our custom command class.
        self.command_class = Command

    # Format --help for the parent command.
    def get_help(self, ctx):
        formatter = HelpFormatter()
        self.format_help(ctx, formatter)
        return formatter.getvalue()


class Command(click.Command):
    """Extends the click.Command class with a custom formatter."""

    # Format --help
    def get_help(self, ctx):
        # pprint(getmembers(self))
        # print(111, self.name)
        formatter = HelpFormatter()
        self.format_help(ctx, formatter)
        # return style(formatter.getvalue(), pad=1, pad_left=2, edge='yellow')
        return formatter.getvalue()
