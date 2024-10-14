"""Type hints intro"""
def calculate_gross_domestic_product(
    personal_consumption_expenditures: float,
    gross_private_domestic_investment: float,
    government_expenditures: float,
    net_exports_of_goods_and_services: float
) -> float:
    """Calculate the gross domestic product (GDP) of a country"""
    return (personal_consumption_expenditures
            + gross_private_domestic_investment
            + government_expenditures
            + net_exports_of_goods_and_services)

print(calculate_gross_domestic_product(100.0, 200.0, 300.0, -100.0))
print(type(calculate_gross_domestic_product(100.0, 200.0, 300.0, -100.0)))
