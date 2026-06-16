print("🏺 Escape the Pyramid 🏺")
print("You are trapped inside an ancient pyramid!")

name = input("What is your name, explorer? ")
print("Welcome", name)

print("\n🏺 Room 1: The Entrance")
print("Solve the riddle to open the door!")

answer1 = input("What has keys but can't open locks? ")

if answer1.lower() == "keyboard":
    print("Correct! The door opens 🚪")
else:
    print("Wrong! Try again next time ❌")
