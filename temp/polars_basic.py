"""Polars basic usage"""
import polars as pl

# Define the file path for clarity
FILE_PATH: str = "/Users/jose.moreno/Documents/Other/UPF/python_101_for_economists/final_project/data_files/train.csv"

# STEP 1: Load and Inspect the Data

#real_estate_data_frame = pl.read_csv(FILE_PATH)
real_estate_data_frame = pl.read_csv(FILE_PATH, null_values=["NA"])
print(real_estate_data_frame)

# Preview the data
print("\nData preview:")
print(real_estate_data_frame.head())
print(real_estate_data_frame.tail())
print(real_estate_data_frame.sample(10))

# Glimpse the data
print("\nData glimpse:")
print(real_estate_data_frame.glimpse(return_as_string=True))

# Check the schema (data types)
print("\nData schema:")
print(real_estate_data_frame.schema)

print("\nData summary:")
print(real_estate_data_frame.describe())

# Numerical Series
price_series = real_estate_data_frame["SalePrice"]
print("\nSalePrice Series:")
print(price_series)

# Categorical Series
ms_zoning_series = real_estate_data_frame["MSZoning"]
print("\nMSZoning Series:")
print(ms_zoning_series)

# Numeric filters
real_estate_data_frame_filtered = real_estate_data_frame.filter(pl.col("SalePrice") < 100000)
print("\nSummary with price filtered < 1000000:")
print(real_estate_data_frame_filtered.describe())
real_estate_data_frame_filtered = real_estate_data_frame.filter(pl.col("SalePrice") < real_estate_data_frame["SalePrice"].quantile(0.95))
print("\nSummary with price filtered < 95% quantile:")
print(real_estate_data_frame_filtered.describe())

# Categorical filters
real_estate_data_frame_filtered = real_estate_data_frame.filter(pl.col("MSZoning") == "RM")
print("\nSummary with MSZoning filtered for Residential Medium Density (RM):")
print(real_estate_data_frame_filtered.describe())

# STEP 2: Cleaning the Data

# Convert "Id" column to integer
real_estate_data_frame = real_estate_data_frame.with_columns(pl.col("Id").cast(pl.Int64))
print("\nSchema with Id as integer:")
print(real_estate_data_frame.schema)

# Rename column Id to id
real_estate_data_frame = real_estate_data_frame.rename({"Id": "id"})
print("\nSchema with Id renamed as id:")
print(real_estate_data_frame.schema)

#Sort data by SalePrice
real_estate_data_frame = real_estate_data_frame.sort(pl.col("SalePrice"), descending=True)
print("\nData sorted by SalePrice (desc):")
print(real_estate_data_frame)

real_estate_data_frame = real_estate_data_frame.sort(pl.col("SalePrice"), descending=False)
print("\nData sorted by SalePrice (asc):")
print(real_estate_data_frame)

# STEP 3: Manipulate the Data

# Fill null values with appropriate defaults
real_estate_data_frame = real_estate_data_frame.fill_null(strategy="zero")
print("\nData with null values filled with 0:")
print(real_estate_data_frame.describe())

# Compute new columns based on other columns
real_estate_data_frame = real_estate_data_frame.with_columns(
    (2024 - pl.col("YearBuilt")).alias("ActualAge"),
    (pl.col("YrSold") - pl.col("YearBuilt")).alias("SoldAge")
)
print("\nData with added ActualAge and SoldAge columns:")
print(real_estate_data_frame.describe())

# Conditionals to create new columns
real_estate_data_frame = real_estate_data_frame.with_columns(
    pl.when(pl.col("SaleCondition") == "Normal")
    .then(False)
    .otherwise(True).alias("NormalSale")
)
print("\nData with added NormalSale column:")
print(real_estate_data_frame.describe())

# Select specific columns
real_estate_data_frame_selected_columns = real_estate_data_frame.select(["id", "SalePrice", "ActualAge", "SoldAge"])
print("\nData with selected columns:")
print(real_estate_data_frame_selected_columns.describe())

# Select, transform and rename columns
select_transform_and_rename = real_estate_data_frame.select(
    time_since_sold=(pl.col("YrSold") - pl.col("YearBuilt")).cast(pl.Int64),
    price_per_sq_ft=pl.col("SalePrice") / pl.col("LotArea")
).rename({"time_since_sold": "TimeSinceSold", "price_per_sq_ft": "PricePerSqFt"})
print("\nData with added TimeSinceSold and PricePerSqFt columns:")
print(select_transform_and_rename.describe())


# STEP 4: Data Analysis
# Group and aggregate data
grouped_data = real_estate_data_frame.group_by("YearBuilt").agg(
    pl.col("SalePrice").mean().alias("MeanSalePrice")
).sort(pl.col("YearBuilt"), descending=True)
print("\nGrouped data by YearBuilt:")
print(grouped_data)

grouped_expansion = real_estate_data_frame.group_by("SaleCondition").agg(
    pl.col("ActualAge", "SoldAge").mean().name.prefix("Mean")
)
print("\nGrouped data with expanded aggregation:")
print(grouped_expansion)

# Calculate correlation
correlation = real_estate_data_frame.select(pl.col("SalePrice", "LotArea")).corr()
print("\nCorrelation between SalePrice and LotArea:")
print(correlation)

#TODO: Theory Homework - Translate this code to pandas. Which code is cleaner? Which library easier to learn?
