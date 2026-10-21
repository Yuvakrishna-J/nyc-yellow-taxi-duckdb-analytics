import duckdb

print("Starting SQL Data Pipeline...")

# 1. Read the query from your new SQL file
with open('clean_taxi_data.sql', 'r') as file:
    sql_query = file.read()

# 2. Execute the query using DuckDB
print("Executing SQL query...")
cleaned_data = duckdb.sql(sql_query)

# 3. Export the cleaned result directly to a new Parquet file
output_file = 'cleaned_yellow_tripdata.parquet'
cleaned_data.to_parquet(output_file)

print(f"Pipeline complete. Cleaned data saved to {output_file}")