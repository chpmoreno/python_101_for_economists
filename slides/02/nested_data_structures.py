"""Nested data structures in Python"""
from typing import List, Tuple, Dict, Set

# Example 1: List of Tuples
# Use case: Representing a dataset with fixed attributes per entry.

# Economic data: (country, Gross Domestic Product (GDP), unemployment_rate)
economic_data: List[Tuple[str, float, float]] = [
    ("USA", 21.43, 3.6),
    ("China", 14.34, 3.8),
    ("Japan", 5.08, 2.4),
    ("Germany", 3.86, 3.2)
]

# Accessing data
print(f"GDP of {economic_data[0][0]}: ${economic_data[0][1]} trillion")

# Example 2: Dictionary with List Values
# Use case: Storing time series data for multiple indicators.
historical_data: Dict[str, List[float]] = {
    "inflation_rate": [1.4, 1.7, 1.9, 2.3, 2.1],
    "gross_domestic_product_growth": [2.3, 2.9, 2.3, 2.2, 2.0],
    "unemployment": [3.9, 3.7, 3.6, 3.5, 3.6]
}

# Calculating average inflation rate
avg_inflation = sum(historical_data["inflation_rate"]) / len(historical_data["inflation_rate"])
print(f"Average inflation rate: {avg_inflation:.2f}%")

# Example 3: Set of Tuples
# Use case: Maintaining a unique collection of data points.

# Trading pairs in a forex (money exchange) market
forex_pairs: Set[Tuple[str, str]] = {
    ("USD", "EUR"),
    ("GBP", "JPY"),
    ("AUD", "CAD"),
    ("EUR", "GBP")
}

# Example 4: Combining List and Dictionary
# Use case: Storing student data with unique IDs and subjects.

students: List[Dict[str, str]] = [
    {"id": "001", "name": "Alice", "subject": "Economics"},
    {"id": "002", "name": "Bob", "subject": "Statistics"},
    {"id": "002", "name": "Bob", "subject": "Statistics"}
]

# Access student data
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Subject: {student['subject']}")

# Example 5: Tuple and Set
# Use case: Tracking coordinates with unique points in space.
coordinates: Set[Tuple[int, int]] = {(10, 20), (15, 25), (10, 20)}

# Print unique coordinates
for coord in coordinates:
    print(f"Coordinate: {coord}")

# Example 6: Combining All Structures
# Use case: Representing a shopping cart with product information.

# ERROR: Unhashable type: 'dict'
# Product = Dict[str, str]
Product = Tuple[str, str]
ShoppingCart = List[Tuple[Product, int]]

# ERROR: Unhashable type: 'dict'
# products: Set[Product] = {
#     {"id": "p1", "name": "Apple"},
#     {"id": "p2", "name": "Banana"}
# }
products: Set[Product] = {
    ("p1", "Apple"),
    ("p2", "Banana")
}

shopping_cart: ShoppingCart = [
    (list(products)[0], 3),
    (list(products)[1], 2)
]

# Print cart details
for product, quantity in shopping_cart:
    print(f"Product: {list(product)[0]}, Quantity: {quantity}")


# Example 7: Dictionary Keys with a Twist (tuples)
student_data: Dict[Tuple[str, str], float] = {
    ("John", "Doe"): 3.8,
    ("Jane", "Smith"): 4.0,
    ("Bob", "Johnson"): 3.9
}

# Print student data
for name, score in student_data.items():
    print(f"Name: {name[0]} {name[1]}, Score: {score}")

# Example 8: Need a unique list of items without duplicates?
mixed_numbers: List[int] = [1, 2, 2, 3, 1, 4]
unique_numbers: Set[int] = set(mixed_numbers)  # Remove duplicates
unique_list: List[int] = list(unique_numbers)  # Convert back to list
print(unique_list)
