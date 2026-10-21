SELECT *
FROM 'yellow_tripdata_2023-01.parquet'
WHERE trip_distance > 0.1 AND trip_distance < 150
  AND fare_amount >= 0 AND fare_amount < 800
  AND passenger_count > 0 AND passenger_count <= 8;