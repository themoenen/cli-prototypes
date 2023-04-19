import json
import curses
from blessed import Terminal

term = Terminal()


def print_json_content(json_content, cursor_pos):
    """Prints the JSON content with the cursor at the specified position."""
    print(111, json_content)
    for i, (key, value) in enumerate(json_content.items()):
        if cursor_pos == i:
            print(term.reverse, end="")
        if isinstance(value, dict):
            print(f"{key}:", term.blue, end="")
            print_json_content(value, cursor_pos - i - 1)
        else:
            print(f"{key}: {term.blue}{value}", end="")
        print(term.normal)
    if cursor_pos == len(json_content):
        print(term.reverse, end="")
    print("")


def edit_json_file(file_path):
    """Edits the specified JSON file using a CLI interface."""
    with open(file_path, "r+") as f:
        json_content = json.load(f)
        cursor_pos = 0

        print_json_content(json_content, cursor_pos)

        with term.cbreak(), term.hidden_cursor():
            while True:
                key_actions = {
                    curses.KEY_UP: lambda: max(cursor_pos - 1, 0),
                    curses.KEY_DOWN: lambda: min(cursor_pos + 1, len(json_content)),
                    # 'KEY_ENTER': lambda: None if isinstance(json_content[cursor_pos], dict) else -1,
                    27: lambda: -1  # Escape key
                }
                for key, action in key_actions.items():
                    print(88, json_content, cursor_pos)
                    result = action()
                    print('\n', 22, key, result, '\n')
                    if key == curses.KEY_UP or key == curses.KEY_DOWN:
                        cursor_pos = result
                    elif key == curses.KEY_ENTER and result is not None:
                        cursor_pos += 1
                    elif result == -1:
                        break

                if cursor_pos == -1:
                    break
                elif cursor_pos == len(json_content):
                    json_content.append("")
                # elif isinstance(json_content[cursor_pos], dict):
                #     continue
                else:
                    # term.move_yx(cursor_pos, term.length(
                    #     list(json_content[cursor_pos].keys())[0]) + 2)
                    value = input(term.blue)
                    json_content[cursor_pos] = value

                term.clear()
                print_json_content(json_content, cursor_pos)

        f.seek(0)
        json.dump(json_content, f, indent=4)
        f.truncate()


# file_path = input("Enter path to JSON file: ")
file_path = 'artist.json'
edit_json_file(file_path)
