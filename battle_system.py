import time, os, random


def main():
    round = 0

    os.system("clear")

    print("⚔️ --- Character Builder --- ⚔️")
    time.sleep(1)

    p1 = createCharacter()
    time.sleep(1)

    print("Who are they battling?")

    p2 = createCharacter()
    time.sleep(4)

    os.system("clear")

    print("⚔️ BATTLE TIME ⚔️")

    time.sleep(1)
    print("\nThe battle begins!\n")

    while True:
        round += 1
        p1Turn, p2Turn = turn(), turn()
        dif = damage(p1["strength"], p2["strength"])
        if p1Turn > p2Turn:
            p2["health"] -= dif
            if round == 1:
                print(f"{p1['name']} wins the first round\n")
            else:
                print(f"{p1['name']} wins round {round}\n")
        elif p1Turn < p2Turn:
            p1["health"] -= dif
            if round == 1:
                print(f"{p2['name']} wins the first round\n")
            else:
                print(f"{p2['name']} wins round {round}\n")
        else:
            print(f"No one wins round {round}\n")

        time.sleep(3)
        print(f"{p1['name']}\nHEALTH: {p1['health']}\n")
        print(f"{p2['name']}\nHEALTH: {p2['health']}\n")

        time.sleep(3)
        if p1["health"] <= 0:
            print(f"{p1['name']} has died!\n")
            print(f"{p2['name']} destroyed {p1['name']} in {round} rounds!")
            break
        elif p2["health"] <= 0:
            print(f"{p2['name']} has died!\n")
            print(f"{p1['name']} destroyed {p2['name']} in {round} rounds!")
            break
        else:
            print("And they're both standing for the next round!")
            time.sleep(3)
            os.system("clear")
            print("The battle continues!\n")
            continue


def rollDice(sides):
    dice = random.randint(1, sides)
    return dice


def healthStatsGenerator():
    health = int(rollDice(6) * rollDice(12) / 2 + 10)
    return health


def strengthStatsGenerator():
    strength = int(rollDice(6) * rollDice(12) / 2 + 12)
    return strength


def createCharacter():
    first_name = input("\nWhat is your character's name?: ").capitalize()
    time.sleep(1)
    type = input(
        "What is your character's type? (Human, Elf, Wiard, Orc): "
    ).capitalize()
    health = healthStatsGenerator()
    strength = strengthStatsGenerator()
    time.sleep(1)
    print(f"\n{first_name} the {type}\nHEALTH: {health}\nSTRENGTH: {strength}\n")
    return {"name": first_name, "type": type, "health": health, "strength": strength}


def turn():
    turn = rollDice(6)
    return turn


def damage(strength1, strength2):
    damage = abs(strength1 - strength2) + 1
    return damage


if __name__ == "__main__":
    main()
