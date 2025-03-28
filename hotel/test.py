import pandas as pd

# Load CSV files
users_df = pd.read_csv("csv_data/users.csv")  # First CSV (user data) csv_data\bookings.csv
bookings_df = pd.read_csv("csv_data/bookings.csv")  # Second CSV (hotel bookings)

# Merge data based on username
merged_df = pd.merge(users_df, bookings_df, on="username", how="left")

# Display merged data
print(merged_df)

# Save merged data to a new CSV
merged_df.to_csv("csv_data/merged_output.csv", index=False)
