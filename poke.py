# poke
# https://pokeapi.co/api/v2/pokemon/ditto
import json
import requests
import sys
from tabulate import tabulate, SEPARATING_LINE


def main():
    """call API"""
    obj = callAPI()

    """ Attributes """
    header = ["CS50's Pokédex"]
    id = obj["id"]
    type = obj["id"]
    name = obj["name"].capitalize()
    sprite = obj["sprites"]["front_default"]
    slen = len(sprite)
    weight = f'{(obj["weight"] * 0.1):10.2f} kg'
    height = f'{obj["height"] * 0.1:10.2f} m'
    moves = get_moves(obj)
    types = get_types(obj)
    stats = get_stats(obj)

    table = [
        ["ID", id],
        ["Name", name],
        ["Type(s)", types],
        ["Height", height],
        ["Weight", weight],
        ["Sprite", sprite],
        SEPARATING_LINE,
        ["Base\nStats", stats],
        SEPARATING_LINE,
        ["Moves", moves],
    ]

    print(tabulate(table, header, maxcolwidths=[None, slen]))


def callAPI() -> dict:
    """
    Promps the user for a str, calls PokeAPI using the str and returns an
    dictionary object of said str, promps again if str is not found.

    :param None: Promts user for input
    :type str: string
    :raise Error: If str is not an found
    :return: A dictionary object
    :rtype: dic
    """
    while True:
        try:
            poke = input("Pokémon Number or Pokémon Name: ")
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke}")
            obj = response.json()
            return obj
        except OSError:
            print("Pokemon not found. Try again")


def get_moves(obj):
    m = len(obj["moves"])
    moves = ""
    for i in range(m):
        moves += obj["moves"][i]["move"]["name"] + " "
    return moves.title().replace(" ", ", ", (m - 1)).strip()


def get_types(obj):
    m = len(obj["types"])
    types = ""
    for i in range(m):
        types += obj["types"][i]["type"]["name"] + " "
    return types.title().replace(" ", " / ", (m - 1)).strip()


def get_stats(obj):
    m = len(obj["stats"])
    stats = ""
    for i in range(m):
        stat = obj["stats"][i]["stat"]["name"]
        base = obj["stats"][i]["base_stat"]
        stats += f"{stat}: {base}  "
    return stats.title().replace("  ", ", ", (m - 1)).strip()


if __name__ == "__main__":
    main()
