# This program computes salaries at a fixed raise each year

# Constants for initial salary, target salary, and yearly raise percentage
start_salary = 16000  # Initial salary in DKK
goal_salary = 25000  # Target salary in DKK
yearly_raise_percentage = 6.5  # Yearly raise percentage in percent (%)

max_years = 10  # Maximum number of years to calculate the salary

current_salary = start_salary  # Set the current salary to the initial salary

# Iterate through each year, including year 0
for year in range(max_years + 1):
    # Display the current salary after each year
    if year == 0:
        print(f"Starting with salary {current_salary} DKK in year {year}")

    # Check if the current salary has reached the target salary
    if current_salary >= goal_salary:
        print(
            f"Reached {current_salary:.2f} DKK after {year} year(s), which is greater than {goal_salary} DKK"
        )

    """
    HOMEWORK #1

    1. Each iteration: use the `print` function to print the value of `salary_raise`
    2. Each iteration, if the value of `current_salary` is less than `goal_salary`:
        use the `print` function to print the result of `goal_salary - current_salary`
    """

    # Calculate the salary raise for the current year
    salary_raise = current_salary * yearly_raise_percentage / 100

    # Homework #1, Part 1: Display the salary raise for the current year
    print(f"Salary raise at the end of year {year}: {salary_raise:.2f} DKK")

    # Homework #1, Part 2: Display the difference between the current salary and the target salary
    if current_salary < goal_salary:
        difference_to_goal = goal_salary - current_salary
        print(f"Amount needed to reach the goal: {difference_to_goal:.2f} DKK")

    # Update the current salary for the next year by adding the salary raise
    current_salary += salary_raise

# Check if the target salary was not reached within the specified number of years
if current_salary < goal_salary:
    print(
        f"Never reached {goal_salary} DKK within {max_years} years, ended at {current_salary:.2f} DKK"
    )
