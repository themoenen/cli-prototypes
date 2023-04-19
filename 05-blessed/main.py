import random

import json
from blessed import Terminal


class Edit_JSON:
    term = Terminal()

    colors = {
        'white': (255, 255, 255),
        'soft_white': (150, 150, 150),
        'black': (0, 0, 0),
        'soft_black': (90, 90, 90),
    }

    styles = {
        'reg': term.on_color_rgb(*colors['black']) + term.color_rgb(*colors['white']),
        'soft': term.on_color_rgb(*colors['black']) + term.color_rgb(*colors['soft_white']),
        'sel': term.on_color_rgb(*colors['white']) + term.color_rgb(*colors['black']),
        'edit': term.on_color_rgb(*colors['soft_black']) + term.color_rgb(*colors['white']),
        'cursor': term.on_color_rgb(*colors['white']) + term.color_rgb(*colors['black']),
    }

    def color(self, color_name, bg=False):
        if bg:
            return self.term.color_rgb(*color_name)
        else:
            return self.term.on_color_rgb(*color_name)

    def __init__(self, path=None):
        # Initialize
        self.edit_mode = False
        self.log_value = ''
        self.selected_index = 0
        self.text_input = ''

        # Get JSON file path.
        if path:
            self.json_file = path
        else:
            self.json_file = input('Enter path to JSON file: ')

        # Store JSON data.
        while True:
            try:
                with open(self.json_file, encoding='UTF-8') as file:
                    self.data = json.load(file)
                    break
            except (FileNotFoundError, json.JSONDecodeError):
                print('Invalid file path or file is not a valid JSON.')

        # print(self.data)

        self.render_list()

    # For debugging: print debug data above the JSON content.
    def log(self, v):
        self.log_value = v

    # Render interactive list of key-value pairs.
    def render_list(self):
        """
        Render interactive list of key-value pairs.
        """

        # Display key-value pairs.
        #
        with self.term.fullscreen(), self.term.cbreak(), self.term.hidden_cursor():
            while True:
                # Clear the console.
                print(self.term.home + self.term.clear)  # + self.term.on_blue
                # print('--', random.randint(0, 100), self.log_value, '\n')
                print('Key:', self.log_value, '\n')

                self.print_list()

                # Store current value.
                selected_key = list(self.data.keys())[self.selected_index]
                selected_value = str(self.data[selected_key])

                # Process user input (ks = keystroke)
                ks = self.term.inkey(timeout=3, esc_delay=0)
                self.log(ks.name or ks)
                if self.edit_mode:
                    # Edit mode
                    if ks.name == 'KEY_ENTER':
                        self.edit_mode = False
                        self.store_value(selected_key, self.text_input)
                        self.update_file()
                    elif ks.name == 'KEY_ESCAPE':
                        self.edit_mode = False
                    elif ks.name == 'KEY_BACKSPACE':
                        self.text_input = self.text_input[:-1]
                        if not self.text_input:
                            self.edit_mode = False
                    elif not ks.is_sequence:
                        self.text_input += ks
                    else:
                        pass

                else:
                    # Browse mode
                    if ks.name == 'KEY_UP':
                        self.selected_index = max(0, self.selected_index - 1)
                    elif ks.name == 'KEY_DOWN':
                        self.selected_index = min(
                            len(self.data) - 1, self.selected_index + 1)
                    elif ks.name == 'KEY_ENTER':
                        self.edit_mode = True
                        # Reset text input.
                        self.text_input = selected_value
                    elif ks.name == 'KEY_ESCAPE':
                        # Exit program.
                        break
                    elif ks and not ks.is_sequence:
                        self.edit_mode = True
                        self.text_input = ks

    # Print list with each keyboard stroke.
    def print_list(self):
        for i, (key, value) in enumerate(self.data.items()):
            if i == self.selected_index:
                # Selected row.
                print(f"{(key + ':'):<20}", end='')
                if self.edit_mode:
                    print(self.styles['edit'] +
                          f" {self.text_input or value}" + self.styles['cursor'] + ' ')
                else:
                    print(self.styles['sel'] +
                          f' {value} ' + self.styles['reg'])
            else:
                # All other rows.
                print(
                    self.styles['soft'] + f"{key + ':':<20} {self.styles['reg'] + str(value)}")

    # Store an edited value on enter.

    def store_value(self, key, value):
        self.data[key] = value.strip()

    # Save changes to json file.
    def update_file(self):
        # Write changes to JSON file.
        with open(self.json_file, 'w') as f:
            json.dump(self.data, f, indent=4)
        print(self.term.green('Changes saved to JSON file.'))


if __name__ == '__main__':
    # Edit_JSON('artist.json')
    Edit_JSON()
