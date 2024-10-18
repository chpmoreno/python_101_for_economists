"""Classes in Python"""
class Car:
    """A class representing a car."""
    def __init__(self, maker: str, model: str):
        """Initialize the Car object with the make and model.

        Args:
            make (str): The maker of the car.
            model (str): The model of the car.
        """
        self.maker = maker
        self.model = model
    def display_info(self) -> None:
        """Print out the make and model of the car."""
        print(f"Car: {self.maker} {self.model}")

car = Car("Toyota", "Camry")
car.display_info()

class Dog:
    """A class representing a dog."""
    def __init__(self, name: str, breed: str) -> None:
        """Initialize the Dog object with a name and breed.

        Args:
            name (str): The name of the dog.
            breed (str): The breed of the dog.
        """
        self.name = name
        self.breed = breed

    def bark(self) -> None:
        """Print a bark sound."""
        print("Woof!")

dog = Dog("Fido", "Poodle")
dog.bark()

class Person:
    """A class representing a person."""
    def __init__(self, name: str, age: int):
        """Initialize the Person object with a name and age.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def greet(self) -> None:
        """Print out a greeting message."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("José", 35)
print(person.age)
print(person.name)
person.greet()
