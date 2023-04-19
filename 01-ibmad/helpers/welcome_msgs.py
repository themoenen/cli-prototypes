"""Welcome messages for each module."""

from workers.style_parser import style
from .ascii_type import ascii_type


#
#


ibmad_welcome: str = """
<h>Welcome to the IBM Accelerated Discovery CLI.</h>

ibmad supports 4 different contexts:
    • <cmd>ds</cmd> - Deep Search
    • <cmd>gt</cmd> - Generative Toolkit
    • <cmd>st</cmd> - Simulation Toolkit
    • <cmd>dc</cmd> - Digital Chemistry

You can access all functionality from the ibmad scope by prepending the context:
    <cmd>ibmad ds <do-xyz></cmd>

You can also switch context:
    <cmd>ibmad enter ds</cmd>
    <cmd><do-xyz></cmd>

To see what you can do:
    <cmd>--help</cmd>
    <cmd>ds --help</cmd>
    <cmd>etc.</cmd>

For comprehensive documention, visit
<link>https://accelerate.science/docs</link>, or run:
    <cmd>--docs</cmd>
"""

ibmad_welcome = style(ascii_type('ibmad') + '\n' +
                      ibmad_welcome, pad=2, pad_left=4, edge=True)


#
#


# Deep search
ds_welcome: str = """
<h>IBM Deep Search CLI</h>

To return to the main Accelerated Discovery CLI:
    <cmd>ibmad enter</cmd>

To see what you can do:
    <cmd>--help</cmd>

For comprehensive documention, visit
<link>https://accelerate.science/ds/docs</link>, or run:
    <cmd>--docs</cmd>
"""
# ds_welcome = style(ascii_type('deep') + '\n' + ascii_type('srch') +
#                    '\n' + ds_welcome, pad=2, pad_left=4, edge=True)
ds_welcome = style(ascii_type('ds') +
                   '\n' + ds_welcome, pad=2, pad_left=4, edge=True)


#
#


# Generative toolkit
gt_welcome: str = """
<h>IBM Generative Toolkit CLI</h>

To return to the main Accelerated Discovery CLI:
    <cmd>ibmad enter</cmd>

To see what you can do:
    <cmd>--help</cmd>

For comprehensive documention, visit
<link>https://accelerate.science/gt/docs</link>, or run:
    <cmd>--docs</cmd>
"""
# gt_welcome = style(ascii_type('genr') + '\n' + ascii_type('tool') +
#                    '\n' + gt_welcome, pad=2, pad_left=4, edge=True)
gt_welcome = style(ascii_type('gt') + '\n' + gt_welcome,
                   pad=2, pad_left=4, edge=True)


#
#


# Simulation toolkit
st_welcome: str = """
<h>IBM Simulation Toolkit CLI</h>

To return to the main Accelerated Discovery CLI:
    <cmd>ibmad enter</cmd>

To see what you can do:
    <cmd>--help</cmd>

For comprehensive documention, visit
<link>https://accelerate.science/st/docs</link>, or run:
    <cmd>--docs</cmd>
"""
# st_welcome = style(ascii_type('simu') + '\n' + ascii_type('tool') +
#                    '\n' + st_welcome, pad=2, pad_left=4, edge=True)
st_welcome = style(ascii_type('st') + '\n' + st_welcome,
                   pad=2, pad_left=4, edge=True)


#
#


# Digital Chemistry
dc_welcome: str = """
<h>IBM Digital Chemistry CLI</h>

To return to the main Accelerated Discovery CLI:
    <cmd>ibmad enter</cmd>

To see what you can do:
    <cmd>--help</cmd>

For comprehensive documention, visit
<link>https://accelerate.science/ds/docs</link>, or run:
    <cmd>--docs</cmd>
"""
# dc_welcome = style(ascii_type('digi') + '\n' + ascii_type('chem') +
#                    '\n' + dc_welcome, pad=2, pad_left=4, edge=True)
dc_welcome = style(ascii_type('dc') + '\n' + dc_welcome,
                   pad=2, pad_left=4, edge=True)
