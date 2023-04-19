"""
Formatter for --help output.

This class overrides the click.HelpFormatter and adds
templated structure and color to the --help output.
"""

import click
from .style_parser import style

# @click.command(cls=Command)

# Source code:
# https://github.com/pallets/click/blob/main/src/click/formatting.py

# Code references:
# https://stackoverflow.com/questions/62182687/custom-help-in-python-click
# https://stackoverflow.com/questions/61933678/categorize-help-output-in-python-click


class HelpFormatter(click.HelpFormatter):
    """ Formats the return for the --help command. """
    colors = {'sep': 'yellow', 'heading': 'green', 'command': 'cyan'}

    def __init__(self, *args):
        super().__init__(*args, indent_increment=4)

    def write_usage(self, prog, *args):
        # print('A')
        """Write usage string."""
        prefix = click.style('Usage: ', fg=self.colors['heading'])
        prog = click.style(prog, fg=self.colors['command'])
        super().write_usage(prog, *args, prefix)

    def write_text(self, text):
        """Write docstring description"""
        # print('B')
        text = style(text)
        super().write_text(text)

    def write_heading(self, heading):
        """Write section heading"""
        # print('C')
        # Copied from source.
        text = f"{'':>{self.current_indent}}{heading}:\n"
        self.write(click.style(text, fg=self.colors['heading']))

    def write_dl(self, rows, *args):
        """Write list of methods"""
        # print('D')
        rows = [tuple([click.style(item[0], fg=self.colors['command']), item[1]])
                for item in rows]
        super().write_dl(rows, *args)

    def getvalue(self):
        """Returns the total --help text"""
        return '\n' + super().getvalue().strip('\n') + '\n'
