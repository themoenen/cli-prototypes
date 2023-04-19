"""
Parse XML style tags for easy styling of text output.

Styles:
<h>I'm a header</h>
<cmd>ibmad ds foobar</cmd>

Colors:
<red>Warning</red>

Supported colors names:
https://click.palletsprojects.com/en/8.1.x/api/#click.style
  • black (might be a gray)
  • red
  • green
  • yellow (might be an orange)
  • blue
  • magenta
  • cyan
  • white (might be light gray)
  • bright_black
  • bright_red
  • bright_green
  • bright_yellow
  • bright_blue
  • bright_magenta
  • bright_cyan
  • bright_white
  • reset (reset the color code only)

"""

import click
from collections import deque
import re


def style(text: str, pad: int = 0, pad_left=0, edge: bool | str = False):
    """
    Parse xml tags and return styled output.

    Parameters:
    • pad (int): Number of line breaks before and after.
    • edge (bool|str): Line left edge with | - can be color or True for white.

    Returns:
    Styled text ready to be published to console via click.echo().
    """
    # Strip any white space at the end
    text = _trim(text)

    # Add left padding
    if pad_left:
        text = _pad_left(text, pad_left)

    # Add edge.
    if edge:
        text = _line(text, edge)

    # Style xml tags
    text = re.sub("(\S*?\s*)<(\w+)>(.+)</\w+>",
                  _repl, text, flags=re.MULTILINE)

    # Add top and bottom padding
    padding = '\n' * pad
    text = padding + text + padding

    return text


def strip(text: str):
    """ Remove all XML tags """
    return re.sub("<\w+>(.+)</\w+>", _strip, text)


#
#
#
#


def _trim(text: str):
    """ Remove line breaks at front/end caused by putting quotes on separate line.  """
    lines = deque(text.split('\n'))

    if lines[0].strip() == '':
        lines.popleft()
    if lines[len(lines) - 1].strip() == '':
        lines.pop()

    return '\n'.join(lines)


def _repl(match: object):
    """ Replace regex matches with appropriate styling. """
    white_space = match.group(1)
    tag = match.group(2)
    inner_text = match.group(3)

    # Set color.
    if tag == 'cmd':
        color = 'cyan'
    # if tag == 'link':
    #     color = 'magenta'
    elif tag == 'h':
        color = None
    else:
        # This is just for debugging, in case an xml tag wasn't defined.
        color = 'magenta'

    # Style text.
    if color:
        styled_text = white_space + click.style(inner_text, fg=color)
    else:
        styled_text = white_space + inner_text

    # Add header lines.
    if tag == 'h':
        styled_text += '\n' + white_space + \
            click.style(('-' * len(inner_text)), fg='yellow') + \
            '\n' + white_space

    return styled_text


def _strip(match: object):
    """ Remove all xml tags. """
    return match.group(1)


def _line(text, edge):
    """ Add liner to left side of a text block. """
    edge_color = 'bright_black' if edge == True else edge
    edge_str = '|'
    edge_str = click.style(edge_str, fg=edge_color)
    return edge_str + f'\n{edge_str}'.join(text.split('\n'))


def _pad_left(text, pad_left):
    """ Add left padding to a text block. """
    spacing = ' ' * pad_left
    return spacing + ('\n' + spacing).join(text.split('\n'))
