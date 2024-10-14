"""Variables introduction"""
GROSS_DOMESTIC_PRODUCT = 1000000000000
UNEMPLOYMENT_RATE = 5.2
COUNTRY_NAME = "United States"
IS_DEVELOPED_COUNTRY = True


def print_variables(
    gross_domestic_product: int,
    unemployment_rate: float,
    country_name: str,
    is_developed_country: bool
) -> None:
    """Print the variables"""
    print(gross_domestic_product)
    print(unemployment_rate)
    print(country_name)
    print(is_developed_country)

def main() -> None:
    """Main function"""
    print_variables(
        gross_domestic_product=GROSS_DOMESTIC_PRODUCT,
        unemployment_rate=UNEMPLOYMENT_RATE,
        country_name=COUNTRY_NAME,
        is_developed_country=IS_DEVELOPED_COUNTRY
    )


if __name__ == "__main__":
    main()
