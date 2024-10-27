# Import libraries
import polars as pl
from polars import DataFrame
from datetime import datetime
import os
from pathlib import Path

# Function that logs body metrics
def log_body_metrics():

    # Take user input
    body_weight = float(input("Enter body weight (in kg): "))
    fat_mass = float(input("Enter fat mass (in %): "))
    water_mass = float(input("Enter water mass (in %): "))
    resting_hr = int(input("Enter resting heart rate (in beats per minute): "))

    # Get today's date in day-month-year format
    todays_date = datetime.today().strftime("%d-%m-%Y")

    # Define height in meters for BMI calculation
    height = 1.85

    # Create a new entry
    new_entry = pl.DataFrame({
        "date": [todays_date],
        "weight": [body_weight],
        "bmi": round(body_weight / (height**2), 2),
        "fat_mass_percentage": [fat_mass],
        "water_percentage": [water_mass]
    })

    # Ensure paths and file directory
    root = Path("log_body_metrics.py").resolve().parent
    processed_data_path = root / "data" / "processed"
    processed_data_path.mkdir(parents=True, exist_ok=True) # Ensure directory exists

    # Check if a previous body metrics file exists
    body_metrics_path = processed_data_path / "body_metrics.csv"

    if body_metrics_path.exists():
        existing_data = pl.read_csv(body_metrics_path)
        updated_data = pl.concat([existing_data, new_entry])
    else:
        updated_data = new_entry

    # Save updated/new data to file
    updated_data.write_csv(body_metrics_path)

log_body_metrics()