import polars as pl
from polars import DataFrame
from pathlib import Path

class StravaDataManager:

    """
    Class to handle data storage and file management for Strava activities.
    """

    def __init__(self, data: DataFrame):
        self.data = data
        self.root = Path(__file__).resolve().parent
        self.raw_data_dir = self.root / "data" / "raw"
        self.raw_data_dir.mkdir(parents=True, exist_ok=True)

    def save_to_csv(self, filename: str = "raw_data.csv") -> None:
        
        """
        Saves the DataFrame to a CSV file.
        
        Args:
            filename (str): Name of the file to save data.
        """

        self.data.to_csv(self.raw_data_dir / filename, index=False)
        print(f"Data saved to {self.raw_data_dir / filename}")

    def is_data_empty(self) -> bool:

        """
        Checks if the DataFrame is empty.

        Returns:
            bool: True if DataFrame is empty, False otherwise.
        """

        return self.data.empty