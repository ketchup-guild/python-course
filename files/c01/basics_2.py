count = 0

while count < 3:

    count = count + 1

    print("This program is going to tell you how long your name is!")

    name = input("Enter your name: ").strip()

    nameLength = len(name)

    if nameLength > 6:
        print(f"WOW, that's a long name! BTW your name is {nameLength} letters long")
        if count == 3:
            print(f"And {name} is a good name to end on!")
    else:
        print(f"The length of {name} is: {nameLength}")

print(f"We did it {count} times, done now!")
