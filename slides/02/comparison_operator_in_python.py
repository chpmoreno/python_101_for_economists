"""Comparison Operators in Economics Example"""

# Economic indicators
GROSS_DOMESTIC_PRODUCT_GROWTH_RATE = 2.5  # Percentage
INFLATION_RATE = 2.0  # Percentage
UNEMPLOYMENT_RATE = 5.5  # Percentage
INTEREST_RATE = 1.5  # Percentage
DEBT_TO_GROSS_DOMESTIC_PRODUCT_RATIO = 80  # Percentage
FOREIGN_INVESTMENT = 50  # Billion dollars

# Target values
TARGET_GROWTH = 3.0
MAX_INFLATION = 2.5
IDEAL_UNEMPLOYMENT = 5.0
MIN_INTEREST_RATE = 1.0
CRITICAL_DEBT_RATIO = 90
DESIRED_INVESTMENT = 60

print("Economic Health Check")
print("-----------------------")

# Equal to (==)
IS_INFLATION_RATE_ON_TARGET = INFLATION_RATE == 2.0
print(f"1. Is the inflation rate at the central bank's target of 2.0%? {IS_INFLATION_RATE_ON_TARGET}")

# Not equal to (!=)
print(f"2. Is the GDP growth rate different from the target growth? {GROSS_DOMESTIC_PRODUCT_GROWTH_RATE != TARGET_GROWTH}")

# Greater than (>)
print(f"3. Is unemployment above the ideal rate? {UNEMPLOYMENT_RATE > IDEAL_UNEMPLOYMENT}")

# Less than (<)
print(f"4. Is foreign investment below the desired level? {FOREIGN_INVESTMENT < DESIRED_INVESTMENT}")

# Greater than or equal to (>=)
print(f"5. Is the interest rate at or above the minimum threshold? {INTEREST_RATE >= MIN_INTEREST_RATE}")

# Less than or equal to (<=)
print(f"6. Is the debt-to-GDP ratio at or below the critical level? {DEBT_TO_GROSS_DOMESTIC_PRODUCT_RATIO <= CRITICAL_DEBT_RATIO}")

# Combining operators
ECONOMY_HEALTHY = (
    GROSS_DOMESTIC_PRODUCT_GROWTH_RATE >= TARGET_GROWTH and
    INFLATION_RATE <= MAX_INFLATION and
    UNEMPLOYMENT_RATE <= IDEAL_UNEMPLOYMENT and
    INTEREST_RATE >= MIN_INTEREST_RATE and
    DEBT_TO_GROSS_DOMESTIC_PRODUCT_RATIO < CRITICAL_DEBT_RATIO and
    FOREIGN_INVESTMENT >= DESIRED_INVESTMENT
)

print(f"\nOverall, is the economy in a healthy state? {ECONOMY_HEALTHY}")
