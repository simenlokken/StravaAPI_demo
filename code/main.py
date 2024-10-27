import logging
from StravaAPI import StravaAPI
from StravaDataManager import StravaDataManager


def main():
    """
    Main function to control the flow of the Strava data fetching and saving process.
    """

    try:
        logging.info("Starting Strava data fetching process...")

        # Instantiate the API class and fetch activities
        strava_api = StravaAPI()
        data = strava_api.get_activities()

        if data.empty:
            logging.warning("No activities were fetched; data is empty.")
            return

        # Instantiate DataManager with the fetched data
        data_manager = StravaDataManager(data)

        # Save the data to a CSV file
        logging.info("Saving data to CSV...")
        data_manager.save_to_csv()

        # Confirm the data was saved and log success
        if data_manager.is_data_empty():
            logging.error("Data was not saved correctly; DataFrame is empty after saving!")
        else:
            logging.info("Data saved successfully. Process completed.")

    except Exception as e:
        logging.exception("An error occurred during the Strava data fetching process.")


if __name__ == "__main__":
    main()