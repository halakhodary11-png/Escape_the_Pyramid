print("🏺 Escape the Pyramid 🏺")
print("You are trapped inside an ancient pyramid!")

name = input("What is your name, explorer? ")
print("Welcome", name)

# Room 1
print("\n🏺 Room 1: The Entrance")
answer1 = input("What has keys but can't open locks? ")

if answer1.lower() == "keyboard":
    print("Correct! The door opens 🚪")
else:
    print("Wrong! You stay in the room ❌")

# Room 2
print("\n🏺 Room 2: The Hieroglyphs Room")
answer2 = input("What ancient writing system did Egyptians use? ")

if answer2.lower() in ["hieroglyphics", "hieroglyphs"]:
    print("Correct! You found a clue 🧠")
else:
    print("Wrong answer ❌")
#room 3
print("\n🏺 Room 3: The Wisdom Room")
answer3 = input("I speak without a mouth and hear without ears. What am I? ")

if answer3.lower() == "echo":
    print("Correct! You passed the wisdom room 🧠")
else:
    print("Wrong answer ❌")
