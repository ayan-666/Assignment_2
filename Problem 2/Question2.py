import os
import pandas as pd

# Set the path to your temperature data folder
temperature_folder = "C:/Users/USER/Downloads/HIT137 Assignment 2 S1 2025"  # Update if your folder structure is different

# Define month-to-season mapping (Australia)
month_to_season = {
    'Jan': 'Summer', 'Feb': 'Summer', 'Mar': 'Autumn',
    'Apr': 'Autumn', 'May': 'Autumn', 'Jun': 'Winter',
    'Jul': 'Winter', 'Aug': 'Winter', 'Sep': 'Spring',
    'Oct': 'Spring', 'Nov': 'Spring', 'Dec': 'Summer'
}

# List to hold all data
all_data = []

# Process each CSV file in the folder
for file_name in os.listdir(temperature_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(temperature_folder, file_name)
        df = pd.read_csv(file_path)
        df.columns = [col.strip() for col in df.columns]

        # Rename columns for months
        month_columns = df.columns[4:]
        renamed_columns = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        df.rename(columns=dict(zip(month_columns, renamed_columns)), inplace=True)
        all_data.append(df)

# Combine all years
combined_df = pd.concat(all_data, ignore_index=True)

# Reshape to long format
melted = pd.melt(combined_df,
                 id_vars=['Station Name', 'Station ID', 'Latitude', 'Longitude'],
                 value_vars=renamed_columns,
                 var_name='Month',
                 value_name='Temperature')

# Clean data
melted.dropna(subset=['Temperature'], inplace=True)
melted['Season'] = melted['Month'].map(month_to_season)
melted['Temperature'] = pd.to_numeric(melted['Temperature'], errors='coerce')

# ----------- Task 1: Average Temp per Season -----------
average_season_temp = melted.groupby('Season')['Temperature'].mean().round(2)

with open("average_temp.txt", "w") as f:
    f.write("Average Temperature by Season Across All Years:\n")
    f.write(average_season_temp.to_string())

# ----------- Task 2: Largest Temp Range Station(s) -----------
station_group = melted.groupby(['Station Name', 'Station ID'])
station_ranges = station_group['Temperature'].agg(['min', 'max'])
station_ranges['range'] = (station_ranges['max'] - station_ranges['min']).round(2)
max_range = station_ranges['range'].max()
largest_range_stations = station_ranges[station_ranges['range'] == max_range]

with open("largest_temp_range_station.txt", "w") as f:
    f.write(f"Station(s) with the Largest Temperature Range ({max_range}°C):\n")
    f.write(largest_range_stations.to_string())

# ----------- Task 3: Warmest and Coolest Stations -----------
station_avg_temp = station_group['Temperature'].mean().round(2)
max_avg = station_avg_temp.max()
min_avg = station_avg_temp.min()

warmest = station_avg_temp[station_avg_temp == max_avg]
coolest = station_avg_temp[station_avg_temp == min_avg]

with open("warmest_and_coolest_station.txt", "w") as f:
    f.write("Warmest Station(s):\n")
    f.write(warmest.to_string())
    f.write("\n\nCoolest Station(s):\n")
    f.write(coolest.to_string())
