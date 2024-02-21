import random


def greet():
    greetings = [
        "Hola",
        "Hello",
        "Hallo",
        "Konnichiwa",
        "Hej",
        "Ciao",
        "Olá",
        "Bonjour",
        "Yassou",
        "Selam",
        "Ahlan",
        "Privet",
        "Nǐ hǎo",
        "Anyoung",
        "Habari",
        "Cześć",
        "Hei",
    ]
    return greetings[random.randint(0, len(greetings)) - 1]


def main():
    name = input("What's your name?: ").capitalize()

    while True:
        text = f"\n{greet()}, {name}!"
        print(f"{text: ^35}\n")
        again = input("Try other language?: y/n ").lower()
        if again == "y":
            continue
        else:
            exit()


if __name__ == "__main__":
    main()
