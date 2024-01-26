def colorful(color, word):
    """ANSI color codes"""
    colors = [
        ["BLACK", "\033[0;30m"],
        ["RED", "\033[0;31m"],
        ["GREEN", "\033[0;32m"],
        ["BROWN", "\033[0;33m"],
        ["BLUE", "\033[0;34m"],
        ["PURPLE", "\033[0;35m"],
        ["CYAN", "\033[0;36m"],
        ["LIGHT_GRAY", "\033[0;37m"],
        ["DARK_GRAY", "\033[1;30m"],
        ["LIGHT_RED", "\033[1;31m"],
        ["LIGHT_GREEN", "\033[1;32m"],
        ["YELLOW", "\033[1;33m"],
        ["LIGHT_BLUE", "\033[1;34m"],
        ["LIGHT_PURPLE", "\033[1;35m"],
        ["LIGHT_CYAN", "\033[1;36m"],
        ["LIGHT_WHITE", "\033[1;37m"],
        ["BOLD", "\033[1m"],
        ["FAINT", "\033[2m"],
        ["ITALIC", "\033[3m"],
        ["UNDERLINE", "\033[4m"],
        ["BLINK", "\033[5m"],
        ["NEGATIVE", "\033[7m"],
        ["CROSSED", "\033[9m"],
        ["END", "\033[0m"],
    ]

    for c in colors:
        if color.upper() == c[0]:
            return f"{c[1]}{word}\033[0m"
    return word


print(
    colorful("bold", "Super Subroutine or function\n"),
    "With my ",
    colorful("purple", "new program "),
    'I can just call red ("and") ',
    colorful("red", "and "),
    "that word will appear in the color I set it to.\n",
    "With no ",
    colorful("cyan", "weird gaps.\n"),
    colorful("yellow", "Epic\n"),
    colorful("faint", "TEST "),
    colorful("negative", "TEST"),
    sep="",
)
print(
    colorful("red", "= MUSIC+ ="),
    colorful("white", "="),
    colorful("bold", "O"),
    colorful("blink", "O"),
)
