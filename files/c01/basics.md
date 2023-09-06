
# Basics

```py
# lines starting with "#" are comments, they are ignored.

# Python reads a file line-by-line

# assign the value `0` to a variable called "count"
count = 0

# this keeps looping the enclosed bluck WHILE the condition `count < 3` is `True`
# we use the variable `count` to count the number of times we have asked for names
# once we have asked for three of them we want to stop the program.
while count < 3:

    # assigns the value of `count + 1` to the variable `count`
    # -> this means that every time the loop runs, the variable `count` increases
    #    i.e. it counts up
    count = count + 1

    # We print text on the console
    print("This program is going to tell you how long your name is!")

    # 1. `input(...)` prints text on the console and waits for the user to enter
    #    text and hit enter.
    # 2. `.strip()` removes spaces from either end of text. Turning " a " into "a"
    # 3. assigns the result to the variable `name`
    name = input("Enter your name: ").strip()

    # 1. `len(...)` determines the length of the text provided as argument
    #    this can be either literal text: `len("abc")` is 3, and 
    #    `name = "abc"` and `len(name)` is also equal to 3.
    # 2. Assignes the result (i.e. the length of the name) to the variable `nameLength`
    nameLength = len(name)

    # If checks a condition and only executes a branch if the condition is True
    if nameLength > 6:
        # This block only runs if the condition is met
        print("WOW, that's a long name!")
    else:
        # This runs only if the condition of the `if` clause ISN'T met
        print(f"The length of {name} is: {nameLength}")

# Note: the following line is not inside the `while` loop above, this means this line
#       is only executed after the loop's condition is no longer met.
print(f"We did it {count} times, done now!")
```

## Lessons

### Execution

Python is executed line by line.

### Variables

```py
# Assign values to variables:
count = 1
average = 2.5
name = "Izabela"

otherCount = count
```

But, variables can change:

```py
count = 3
count = count + 1
# `count` is now 4
```

### Console IO

```py
# Prints text on the screen
print("Hello world")

# Can also print variables
message = "This is a message"
print(message) 

# Using format strings (more about those later) we can include variables
count = 420
print(f"The count is {count}") # prints "The count is 420"
```

We can also read user input

```py
name = input("Enter your name: ") # Prompts the user to enter text, stores it in the variable.
```

### Text processing

```py
# Determine the length of text
nameLength = len("Markus") # is 6

name = "Ida"
nameLength = len(name) # is 3
```

```py
# Concatenate text
message = "My name is " + "Markus" # is "My name is Markus"

# also works with variables
name = "Markus"
message = "My name is " + name # also is "My name is Markus"

# we can use format strings
name = "Markus"
message = f"My name is {name}" # also is "My name is Markus"

# Be weary of numbers (and other types of data)
# this DOES NOT work:
message = "My age is " + 26
# you cannot "add" text and numbers!
# Instead, convert numbers to text first:
message = "My age is " + str(26) # is "My age is 26"
# or use format strings:
message = f"My age is {26}" # also is "My age is 26"
```

### Conditional execution

```py
# The code in `block` is only executed if the `condition` is True
if condition:
    block

# We can add an else block to execute if the `condition` is False
if condition:
    block1
else:
    block2
```

### Loops

```py
# The while loop keeps execution the block "while" the condition is True.
# The condition is evaluated once before each execution of the `block`.
# Afterwards, execution continues below the `while` loop's `block`.
while condition:
    block
```
