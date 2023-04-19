
# key_actions = {
#     term.KEY_UP: lambda: max(cursor_pos - 1, 0),
#     term.KEY_DOWN: lambda: min(cursor_pos + 1, len(json_content)),
#     term.KEY_ENTER: lambda: None if isinstance(json_content[cursor_pos], dict) else -1,
#     term.KEY_ESCAPE: lambda: -1
# }
# for k, v in key_actions.items():
#     term.on(k)(lambda v=v: setattr(cursor_pos, "value", v()))
