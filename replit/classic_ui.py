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


header = f'{colorful("red","=")}{colorful("black", "=")}{colorful("blue", "=")} {colorful("black", "Music App")} {colorful("blue", "=")}{colorful("black", "=")}{colorful("red","=")}'
song = f'{colorful("black", "Radio Gaga")}'
artist = f'{colorful("yellow", "Queen")}'
prev = "PREV"
next = f'{colorful("green", "NEXT")}'
pause = f'{colorful("purple", "PAUSE")}'

print()
print(f"{header: ^100}")
print()
print(f"🔥▶️\t {song}")
print(f"\t{artist}")
print(f"\n{prev: <35}")
print(f" {next: ^35}")
print(f" {pause: >35}")

print("\n\n\n\n")

header2 = f'{colorful("black","WELCOME TO")}'
header3 = f'{colorful("blue", "--   ARMBOOK   --")}'
text1 = f'{colorful("yellow", "Definitely not a rip off of")}'
text2 = f'{colorful("yellow", "     a certain other social")}'
text3 = f'{colorful("yellow", "           networking site.")}'
text4 = f'{colorful("red", "Honest.")}'
username = f'{colorful("black","Username:")}'
password = f'{colorful("black","Password:")}'

print(f"{header2: ^35}")
print(f"{header3: ^35}")
print()
print(f"{text1: >35}")
print(f"{text2: >35}")
print(f"{text3: >35}")
print()
print(f"{text4: ^35}")
print()
print(f"{username: ^35}")
print(f"{password: ^35}")
print()
