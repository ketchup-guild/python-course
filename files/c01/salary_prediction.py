# This program computes salaries at a fixed raise each year

# = to assign value to a variable
start_salary = 16000  # in DKK
goal_salary = 25000  # in DKK
yearly_raise_percentage = 6.5  # in percent (%)

max_years = 10

current_salary = start_salary

for year in range(max_years + 1):  # range starts at 0
    # Show `current_salary` after `year` years
    if year == 0:  # == compares
        print(f"Starting with salary {current_salary} DKK in year {year}")

    if current_salary >= goal_salary:
        print(
            f"Reached {current_salary:.2f} DKK after {year} year(s), which is greater than {goal_salary} DKK"
        )

    salary_raise = current_salary * yearly_raise_percentage / 100

    # read this as "set current_salary to whatever current_salary is plus salary_raise"
    current_salary = current_salary + salary_raise

if current_salary < goal_salary:
    print(
        f"Never reached {goal_salary} DKK within {max_years} years, ended at {current_salary:.2f} DKK"
    )
