# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list

def loan_count(loan_info):
    number_of_loans = len(loan_info)
    return number_of_loans

def loan_count_print(loan_info_1):
    number_of_loans_1 = loan_count(loan_info_1)
    print(f"There is a total of {number_of_loans_1} loans.")

loan_count_print(loan_costs)

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

def loan_total(loan_data):
    total_of_loans = sum(loan_data)
    return total_of_loans

def loan_total_print(loan_data_1):
    total_of_loans_1 = loan_total(loan_data_1)
    print(f"The loans sum to a total of ${total_of_loans_1: .2f}.")

loan_total_print(loan_costs)

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

def loan_average (loan_material):
    average_of_loans = loan_total(loan_material)/loan_count(loan_material)
    return average_of_loans

def loan_average_print(loan_material_1):
    average_of_loans_1 = loan_average(loan_material_1)
    print(f"The average loan price is ${average_of_loans_1: .2f}.")

loan_average_print(loan_costs)

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

def future_value(loan_1):
    fv = loan_1.get("future_value")
    return fv

def future_value_print(loan_2):
    fv_1 = future_value(loan_2)
    print(f"The future value of the loan is ${fv_1: .2f}.")

future_value_print(loan)

def remaining_months(loan_3):
    rm = loan_3.get("remaining_months")
    return rm

def remaining_months_print(loan_4):
    rm_1 = remaining_months(loan_4)
    print(f"The months remaining on the loan is {rm_1} months.")

remaining_months_print(loan)

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
discount_rate = 0.20
def present_value(loan_5):
    pv = future_value(loan_5) / ((1 + discount_rate/12) ** remaining_months(loan_5))
    return pv

def present_value_print(loan_6):
    pv_1 = present_value(loan_6)
    print(f"The present value of the loan is ${pv_1: .2f} given a future value of ${future_value(loan_6): .2f}, a discount rate of {discount_rate * 100: .2f}%, and {remaining_months(loan_6)} months remaining.")

present_value_print(loan)

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

def loan_cost(loan_7):
    lc = loan_7.get("loan_price")
    return lc

def loan_cost_print(loan_8):
    lc_1 = loan_cost(loan_8)
    print(f"The cost of the loan is ${lc_1: .2f}.")

loan_cost_print(loan)

def buy_nobuy_loan(loan_9):
    if present_value(loan_9) >= loan_cost(loan_9):
        print(f"The loan is worth at least the cost to buy it.")
        #loan_cost_print(loan_9)
        #present_value_print(loan_9)
    else:
        print(f"The loan is too expensive and not worth the price.")
        #loan_cost_print(loan_9)
        #present_value_print(loan_9)

buy_nobuy_loan(loan)

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# I already created the present_value and present_value_print functions.
# I am creating the next function to satisfy the above specifications for the assignment.

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(fv_2, rm_2, discount_rate_1):
    pv_2 = fv_2 / ((1 + discount_rate_1/12) ** rm_2)
    return pv_2 # I already created the present_value function. I am creating this function to satisfy the above specifications for the assignment.
# present_value(new_loan) # accomplishes the same
# print(f"${present_value(new_loan): .2f}") # prints the returned value with a dollar sign and two decimal places

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
annual_discount_rate = 0.20
present_value_1 = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)
print(f"The present value of the loan is: ${present_value_1: .2f}") # I already created the present_value_print function. I am creating this function to satisfy the above specifications for the assignment.
# present_value_print(new_loan) # performs a similar print statement with additional details

"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    loan_price = loan.get("loan_price")
    if loan_price <= 500:
        inexpensive_loans.append(loan)

# @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
