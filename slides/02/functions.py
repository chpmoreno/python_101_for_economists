"""Functions in Python"""
from typing import Optional

def greet(name: str) -> None:
    """Greets a person by name.
    Args:
        name (str): The name of the person to greet.
    """
    print(f"Hello, {name}!")

greet(name="Raul")  # Output: Hello, Raul!

def add_numbers(number_1: int, number_2: int) -> int:
    """
    Adds two numbers and returns the result.
    
    Args:
        number_1 (int): The first number
        number_2 (int): The second number
    
    Returns:
        int: The sum of number_1 and number_2
    """
    return number_1 + number_2

# Positional arguments
RESULT_1 = add_numbers(10, 5)
print(RESULT_1) # Output: 15

# Keyword arguments
RESULT_2 = add_numbers(number_1=10, number_2=5)
print(RESULT_2) # Output: 15

def calculate_area(length: int, width: int) -> int:
    """Calculates the area of a rectangle.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        int: The area of the rectangle.
    """
    area = length * width
    return area

RECTANGLE_AREA = calculate_area(4, 6)
print(RECTANGLE_AREA)  # Output: 24

def greet_with_message(
    name: str = "Guest",
    message: str = "",
    age: Optional[int] = None
) -> None:
    """Prints a greeting message with a name and an optional message.

    Args:
        name (str): The name of the person to greet. Defaults to "Guest".
        message (str): The message to use. Defaults to "Welcome!".
        age (int, optional): The age of the person. Defaults to None.
    """
    if not message:
        message = "Welcome!"
    if age:
        print(f"{message}, {name}! I am {age} years old.")
    else:
        print(f"{message}, {name}!")

greet_with_message()  # Output: Welcome!, Guest!
greet_with_message("Raul")  # Output: Welcome!, Raul!
greet_with_message("Paula", "Hello")  # Output: Hello, Paula!
greet_with_message(
    name="José",
    message="Hello",
    age=35
)
