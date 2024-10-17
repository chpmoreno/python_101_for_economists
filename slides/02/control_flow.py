"""Control Flow in Python"""
from typing import Tuple, List

# Conditional Statements
def classify_growth(
    country: str,
    gross_domestic_product_growth: float
) -> Tuple[str, str]:
    if gross_domestic_product_growth > 0.03:
        category = "High growth"
    elif 0.01 <= gross_domestic_product_growth <= 0.03:
        category = "Moderate growth"
    elif 0 <= gross_domestic_product_growth < 0.01:
        category = "Slow growth"
    else:
        category = "Recession"
    return (country, category)

# Example usage
result = classify_growth("USA", 0.023)
print(f"{result[0]} economy: {result[1]}")

# Looping
def calculate_compound_interest_for_loop(
    principal: float,
    rate: float,
    years: int
) -> List[float]:
    balance: List[float] = [principal]
    for _ in range(years):
        new_balance = balance[-1] * (1 + rate)
        balance.append(round(new_balance, 2))
    return balance

def calculate_compound_interest_while_loop(
    principal: float,
    rate: float,
    years: int
) -> List[float]:
    balance: List[float] = [principal]
    year: int = 0
    while year <= years:
        new_balance = balance[-1] * (1 + rate)
        balance.append(round(new_balance, 2))
        year += 1
    return balance

# Example usage
result = calculate_compound_interest_for_loop(1000, 0.05, 10)
for year, amount in enumerate(result):
    print(f"Year {year}: ${amount:.2f}")
result = calculate_compound_interest_while_loop(1000, 0.05, 10)
for year, amount in enumerate(result):
    print(f"Year {year}: ${amount:.2f}")

# List comprehensions
squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares)

# Dictionary comprehensions
numbers = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(numbers)

# Set comprehensions
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)

# Tuple comprehensions
tuples = [(x, x + 1) for x in range(10) if x % 2 == 0]
print(tuples)

# Functions
# Lists are ordered collections of elements.
# You can iterate through them with a for loop.
def list_iteration(prices: list[float]) -> None:
    for price in prices:
        print(f"Price: ${price}")

price_list = [12.99, 19.99, 3.50]
list_iteration(price_list)

# Sets are unordered collections of unique elements. Since sets do not maintain any order,
# you can still iterate through them with a for loop, but the order of elements may change.
def set_iteration(countries: set[str]) -> None:
    for country in countries:
        print(f"Country: {country}")

country_set = {"France", "Japan", "Germany"}
set_iteration(country_set)

# Dictionaries are collections of key-value pairs. You can iterate over:
# Keys, Values and Key-Value Pairs
def dict_iteration(economic_data: dict[str, float]) -> None:
    # Iterate over keys
    for key in economic_data.keys():
        print(f"Key: {key}")
    # Iterate over values
    for value in economic_data.values():
        print(f"Value: {value}")
    # Iterate over key-value pairs
    for key, value in economic_data.items():
        print(f"{key}: {value}")

economic_data_dictionary = {"GDP": 21000.5, "Inflation": 2.3, "Unemployment": 5.1}
dict_iteration(economic_data_dictionary)

# enumerate function
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# zip function
countries_list = ["France", "Japan", "Germany"]
prices_list = [12.99, 19.99, 3.50]
for country_value, price_value in zip(countries_list, prices_list):
    print(f"{country_value}: ${price_value}")
