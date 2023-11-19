input_file = "files/c01/aoc_2020_01_input.txt"

# 1. Read the input file, convert all the lines to numbers
file_handle = open(input_file)
lines = file_handle.readlines()
numbers = [int(line.strip()) for line in lines]

# 2. Try all combinations of two numbers, until we find one that adds to 2020
count_of_numbers = len(numbers)
first_index = 0

print(f"Number of lines: {count_of_numbers}")
while first_index < count_of_numbers:
    first_number = numbers[first_index]
    second_index = first_index + 1
    while second_index < count_of_numbers:
        second_number = numbers[second_index]
        sum_of_numbers = first_number + second_number

        # Solves pair of 2 that add to 2020
        if sum_of_numbers == 2020:
            print(f"We found the pair: {first_number} + {second_number} = 2020 (at numbers[{first_index}], numbers[{second_index}])")
            solution = first_number * second_number
            print(f"The solution for the first part is: {solution}")

        third_index = second_index + 1
        while third_index < count_of_numbers:
            third_number = numbers[third_index]

            sum_of_tripplet = first_number + second_number + third_number

            # Solves tripplet that add to 2020
            if sum_of_tripplet == 2020:
                print(f"We found the tripplet: {first_number} + {second_number} + {third_number} = 2020 (at numbers[{first_index}], numbers[{second_index}], numbers[{third_index}])")
                solution = first_number * second_number * third_number
                print(f"The solution for the second part is: {solution}")
            
            third_index = third_index + 1

        second_index = second_index + 1

    first_index = first_index + 1
