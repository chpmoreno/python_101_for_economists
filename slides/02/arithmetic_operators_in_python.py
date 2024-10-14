"""Arithmetic Operators in Economics Example"""

# Initial economic values
GROSS_DOMESTIC_PRODUCT = 1000000000000  # $1 trillion
POPULATION = 331000000
GOVERNMENT_DEBT = 23000000000000  # $23 trillion
TAX_RATE = 0.15  # 15%
INFLATION_RATE = 0.02  # 2%
YEARS = 5

# Addition (+): Calculate total government revenue
INCOME = 50000
TAX_REVENUE = INCOME * TAX_RATE
GOVERNMENT_SPENDING = 4000000000000  # $4 trillion
TOTAL_GOVERNMENT_REVENUE = TAX_REVENUE + GOVERNMENT_SPENDING
print(f"1. Addition (+): Total government revenue = ${TOTAL_GOVERNMENT_REVENUE}")

# Subtraction (-): Calculate budget deficit
BUDGET_DEFICIT = GOVERNMENT_SPENDING - TOTAL_GOVERNMENT_REVENUE
print(f"2. Subtraction (-): Budget deficit = ${BUDGET_DEFICIT:.2f}")

# Multiplication (*): Calculate GDP after 5 years of consistent growth
GROSS_DOMESTIC_PRODUCT_GROWTH_RATE = 0.03  # 3% annual growth
FUTURE_GROSS_DOMESTIC_PRODUCT = GROSS_DOMESTIC_PRODUCT * (1 + GROSS_DOMESTIC_PRODUCT_GROWTH_RATE) ** YEARS
print(f"3. Multiplication (*): GDP after {YEARS} years = ${FUTURE_GROSS_DOMESTIC_PRODUCT:.2f}")

# Division (/): Calculate GDP per capita
GROSS_DOMESTIC_PRODUCT_PER_CAPITA = GROSS_DOMESTIC_PRODUCT / POPULATION
print(f"4. Division (/): GDP per capita = ${GROSS_DOMESTIC_PRODUCT_PER_CAPITA:.2f}")

# Floor Division (//): Calculate whole number of years to double GDP
YEARS_TO_DOUBLE = 72 // (GROSS_DOMESTIC_PRODUCT_GROWTH_RATE * 100)  # Using the Rule of 72 https://www.investopedia.com/terms/r/ruleof72.asp
print(f"5. Floor Division (//): Years to double GDP = {YEARS_TO_DOUBLE}")

# Modulus (%): Calculate remaining debt after paying full $1 trillion installments
FULL_PAYMENTS = GOVERNMENT_DEBT // 1000000000000
REMAINING_DEBT = GOVERNMENT_DEBT % 1000000000000
print(f"6. Modulus (%): Remaining debt after {FULL_PAYMENTS} trillion-dollar payments = ${REMAINING_DEBT}")

# Exponentiation (**): Calculate compound interest on an investment
INITIAL_INVESTMENT = 10000
INTEREST_RATE = 0.05  # 5% annual interest
INVESTMENT_DURATION = 10  # years
FUTURE_VALUE = INITIAL_INVESTMENT * (1 + INTEREST_RATE) ** INVESTMENT_DURATION
print(f"7. Exponentiation (**): Investment future value = ${FUTURE_VALUE:.2f}")
