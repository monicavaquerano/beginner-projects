print("30 Days Down - What did you think?")

for i in range(1, 31):
    print(f"\nDay {i}:")
    response = input()
    print()
    text = f"You thought Day {i} was"
    print(f"{text: ^35}")
    print(f"{response: ^35}")
