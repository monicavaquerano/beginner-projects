from colorful import colorful


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
