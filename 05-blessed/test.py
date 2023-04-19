from blessed import Terminal

term = Terminal()

# print(term.green_reverse(' ALL SYSTEMS GO '))
# print(term.white_on_firebrick3('SYSTEM OFFLINE'))
# print(term.color_rgb(60, 255, 60)('SYSTEM OFFLINE'))
# print(f"{term.yellow}Yellow is brown, {term.bright_yellow}"
#       f"Bright yellow is actually yellow!{term.normal}")
# print(term.blink("Insert System disk into drive A:"))
# print(term.underline_bold_green_on_yellow('They live! In sewers!'))
# print(
#     f"blessed {term.link('https://blessed.readthedocs.org', 'documentation')}")
# print(term.number_of_colors == 1 << 24)


# print(f"{term.home}{term.black_on_skyblue}{term.clear}")
# print("press 'q' to quit.")
# with term.cbreak():
#     val = ''
#     while val.lower() != 'q':
#         val = term.inkey(timeout=3)
#         if not val:
#             print("It sure is quiet in here ...")
#         elif val.is_sequence:
#             print("got sequence: {0}.".format((str(val), val.name, val.code)))
#         elif val:
#             print("got {0}.".format(val))
#     print(f'bye!{term.normal}')

# print(term.home + term.clear, end='')
# print(term.move_down(2) + term.move_right(20) +
#       term.bright_red('fire!'), end='')
# print(term.move_xy(20, 7) + term.bold('Direct hit!'), end='')
# print(term.move_y(term.height - 3), end='')


# with term.location(0, term.height - 3):
#     print('Here is the bottom.')
# print('This is back where I came from.')

# with term.location():
#     print(term.move_xy(1, 1) + 'Hi Mom!' + term.clear_eol)
