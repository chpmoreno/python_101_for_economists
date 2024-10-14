"""Why Python for Economist"""
from typing import Callable, Tuple
import numpy as np
import matplotlib.pyplot as plt

def linear_function(intercept: float, slope: float) -> Callable[[float], float]:
    """
    Generate a linear function of the form f(x) = intercept - slope * x
    
    :param intercept: Y-intercept of the linear function
    :param slope: Slope of the linear function
    :return: A function that takes a float as input and returns a float
    """
    return lambda x: intercept + slope * x

def find_equilibrium(
    supply_function: Callable[[float], float],
    demand_function: Callable[[float], float],
    start_guess: float = 0,
    max_iter: int = 100,
    tol: float = 1e-5
) -> Tuple[float, float]:
    """
    Find the equilibrium point where the supply equals demand using the bisection method.
    
    :param supply_function: The supply function that takes quantity and returns price
    :param demand_function: The demand function that takes quantity and returns price
    :param start_guess: Initial guess for the equilibrium quantity
    :param max_iter: Maximum number of iterations
    :param tol: Tolerance level for convergence
    :return: Equilibrium quantity and price as a tuple
    """
    low, high = start_guess, start_guess + 100
    for _ in range(max_iter):
        mid = (low + high) / 2
        if abs(supply_function(mid) - demand_function(mid)) < tol:
            equilibrium_quantity_mid = mid
            equilibrium_price_mid = supply_function(equilibrium_quantity_mid)
            return equilibrium_quantity_mid, equilibrium_price_mid
        elif supply_function(mid) > demand_function(mid):
            high = mid
        else:
            low = mid
    raise ValueError("Equilibrium not found within the maximum number of iterations")

def plot_supply_demand(
    supply_function: Callable[[float], float],
    demand_function: Callable[[float],float],
    equilibrium_quantity: float,
    equilibrium_price: float
) -> None:
    """
    Plot the supply and demand curves and mark the equilibrium point.
    
    :param supply_function: The supply function that takes quantity and returns price
    :param demand_function: The demand function that takes quantity and returns price
    :param equilibrium_quantity: The equilibrium quantity
    :param equilibrium_price: The equilibrium price
    """
    quantities = np.linspace(0, equilibrium_quantity * 2, 100)
    supply_prices = np.array([supply_function(q) for q in quantities])
    demand_prices = np.array([demand_function(q) for q in quantities])
    plt.figure(figsize=(10, 6))
    plt.plot(quantities, supply_prices, label='Supply Curve', color='blue')
    plt.plot(quantities, demand_prices, label='Demand Curve', color='orange')
    plt.scatter(
        [equilibrium_quantity],
        [equilibrium_price],
        color='red',
        s=100,
        label='Equilibrium Point'
    )
    plt.title('Supply and Demand Curves with Equilibrium Point')
    plt.xlabel('Quantity')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.annotate(
        f'Equilibrium ({equilibrium_quantity:.2f}, {equilibrium_price:.2f})',
        xy=(equilibrium_quantity, equilibrium_price),
        xytext=(5, 5),
        textcoords='offset points'
    )
    plt.show()

# Define supply and demand functions using linear models
supply_function_linear = linear_function(intercept=20, slope=1.5)  # Supply: P(Q) = 20 + 1.5Q
demand_function_linear = linear_function(intercept=80, slope=-2.0)  # Demand: P(Q) = 80 - 2.0Q

# Find the equilibrium price and quantity
equilibrium_quantity_solution, equilibrium_price_solution = find_equilibrium(
    supply_function_linear,
    demand_function_linear
)
print(f"Equilibrium Quantity: {equilibrium_quantity_solution:.2f}")
print(f"Equilibrium Price: {equilibrium_price_solution:.2f}")

# Plot the supply and demand curves
plot_supply_demand(
    supply_function_linear,
    demand_function_linear,
    equilibrium_quantity_solution,
    equilibrium_price_solution
)
