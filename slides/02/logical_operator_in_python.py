"""Comparison Operators in Economics Example"""
# Economic indicators
GDP_GROWTH = 2.5  # Percentage
INFLATION = 2.0   # Percentage
UNEMPLOYMENT = 5.5  # Percentage

# Thresholds for a healthy economy
MIN_GDP_GROWTH = 2.0
MAX_INFLATION = 3.0
MAX_UNEMPLOYMENT = 6.0

# Using logical operators to check economic conditions

# AND operator: All conditions must be true
ECONOMY_HEALTHY = (
    GDP_GROWTH > MIN_GDP_GROWTH and
    INFLATION < MAX_INFLATION and
    UNEMPLOYMENT < MAX_UNEMPLOYMENT
)
print(f"Is the economy healthy? {ECONOMY_HEALTHY}")

# OR operator: At least one condition must be true
NEEDS_STIMULUS = (
    GDP_GROWTH < MIN_GDP_GROWTH or
    UNEMPLOYMENT > MAX_UNEMPLOYMENT
)
print(f"Does the economy need stimulus? {NEEDS_STIMULUS}")

# NOT operator: Inverts a boolean value
INFLATION_UNDER_CONTROL = not INFLATION > MAX_INFLATION
print(f"Is inflation under control? {INFLATION_UNDER_CONTROL}")

# Combining operators
COMPLEX_CONDITION = (
    (GDP_GROWTH > MIN_GDP_GROWTH and INFLATION < MAX_INFLATION) or
    not UNEMPLOYMENT > MAX_UNEMPLOYMENT
)
print(f"Complex economic condition met? {COMPLEX_CONDITION}")
