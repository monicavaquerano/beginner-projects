"""
👉 Day 65 Challenge
Today is a project day! You're going to use what you've learned about OOP (on Day 64) to store characters for my video game.

1. My game needs to have a character with a name, health and magic points.
2. It needs these values setup when it is initialized.
3. It needs a method to output this data.
4. There should be a sub-class 'player' which inherits from character and also has a number of lives.
5. Player should also have an 'am I alive?' method which checks the player status and reports back yes or no.
6. There should also be an 'enemy' sub-class with additional 'type' and 'strength'.
7. 'enemy' should have two sub-classes:
    i. 'orc' with a 'speed' attribute.
    ii. 'vampire' with a 'day/night' tracker
8. Instantiate one player, two vampires and three orcs. You choose their names.
9. Print out their values.

Example:
🌟Generic RPG🌟
Player
Name: David
Health: 100
Magic Points: 50
Lives: 3
Alive?: Yes

Hints:
You only need to inherit from the class dierctly above. So orc only needs to inherit from enemy, for example.

More examples:
Name: Boris
Health: 45
Magic Points: 70
Type: Vampire
Strength: 3
Day/Night?: Night

Name: Rishi
Health: 70
Magic Points: 10
Type: Vampire
Strength: 75
Day/Night?: Day

Name: Bill
Health: 60
Magic Points: 5
Type: Orc
Strength: 75
Speed: 90

Name: Ted
Health: 75
Magic Points:40
Type: Orc
Strength: 80
Speed: 45

Name: Station
Health: 35
Magic Points: 40
Type: Orc
Strength: 49
Speed: 50
"""

import time


class Character:
    name: str = None
    health: int = 0
    magicPoints: int = 0

    def __init__(self, name) -> None:
        self.name = name

    def setStats(self, health, mp):
        self.health = int(health)
        self.magicPoints = int(mp)

    def print(self):
        print("🌟 Generic RPG 🌟")
        print(
            f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}"
        )
        print()


class Player(Character):
    nickname: str = None
    lives: int = 0

    def __init__(
        self,
        name,
    ) -> None:
        super().__init__(name)

    def setStats(self, health, mp, lives, nickname):
        super().setStats(health, mp)
        self.lives = int(lives)
        self.nickname = nickname

    def isAlive(self):
        return self.lives > 0

    def print(self):
        print("🌟 Player 🌟")
        print(
            f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}"
        )
        print(f"Nickname: {self.nickname}")
        print(f"Lives: {self.lives}")
        print(f"Is alive?: {self.isAlive()}")
        print()


class Enemy(Character):
    type: str = None
    strength: int = None

    def __init__(self, name, type, strength) -> None:
        super().__init__(name)
        self.type = type
        self.strength = strength


class Orc(Enemy):
    type = None
    speed: int = None

    def __init__(self, name, strength, speed) -> None:
        self.name = name
        self.strength = strength
        self.speed = speed
        self.type = "Orc"

    def print(self):
        print("🌟 Orc 🌟")
        print(
            f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}"
        )
        print(f"Type: {self.type}")
        print(f"Strength: {self.strength}")
        print(f"Speed: {self.speed}")
        print()


class Vampire(Enemy):
    type = None
    day: bool = 6 < int(time.strftime("%H")) < 18

    def __init__(self, name, strength) -> None:
        self.name = name
        self.strength = strength
        self.type = "Vampire"

    def print(self):
        print("🌟 Vampire 🌟")
        print(
            f"Name: {self.name}\nHealth: {self.health}\nMagic Points: {self.magicPoints}"
        )
        print(f"Type: {self.type}")
        print(f"Strength: {self.strength}")
        print(f"Day?: {self.day}")
        print()


# 1 player: bob
bob = Player("Bob")
bob.setStats(health="10", mp="20", lives="3", nickname="Bobby")
bob.print()

# 2 vampire: louis, lestat
louis = Vampire(name="Louis", strength=50)
louis.setStats(health=50, mp=50)
louis.print()

lestat = Vampire(name="Lestat", strength=50)
lestat.setStats(health=75, mp=50)
lestat.print()

# 3 orcs: sharon, gary, felicity
sharon = Orc(name="Sharon", speed=40, strength=60)
sharon.setStats(health=85, mp=33)
sharon.print()

gary = Orc(name="Gary", speed=20, strength=90)
gary.setStats(health=85, mp=33)
gary.print()

felicity = Orc(name="Felicity", speed=90, strength=50)
felicity.setStats(health=85, mp=33)
felicity.print()
