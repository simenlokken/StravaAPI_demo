import requests
import os
import pandas as pd
from pandas import DataFrame
from pathlib import Path

class StravaAPI:

    """
    Contains instances and methods that interact with Strava v3 API.
    Handles authentication and fetches activities.
    """

    def __init__(self) -> None:
        self.client_id = os.getenv("STRAVA_CLIENT_ID")
        self.client_secret = os.getenv("STRAVA_CLIENT_SECRET")
        self.refresh_token = os.getenv("STRAVA_REFRESH_TOKEN")
        self.auth_url = "https://www.strava.com/oauth/token"
        self.base_url = "https://www.strava.com/api/v3"
        self.access_token = self._fetch_access_token()

    def fetch_access_token(self) -> str:

        """
        Fetches an access token with a POST request using the refresh token you get from your Strava Application.        
        """

        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
            'grant_type': "refresh_token",

        }

        result = requests.post(url=self.auth_url, data=payload)
        result.raise_for_status()
        return result.json()["access_token"]
    
    def get_activities(self, per_page: int = 200) -> DataFrame:

        """
        Fetches all Strava activities and returns them as a DataFrame.
        
        Args:
            per_page (int): Number of activities per request, default is 200.

        Returns:
            DataFrame: A Pandas DataFrame with the fetched activities.
        """

        activities = []
        page = 1

        while True:
            response = requests.get(
                url=f"{self.base_url}/athlete/activities",
                headers={"Authorization": f"Bearer {self.access_token}"},
                params={"per_page": per_page, "page": page},
            )

            if response.status_code != 200:
                print(f"Error fetching activities: {response.status_code}")
                break

            data = response.json()

            if not data:
                break

            activities.extend(data)
            page += 1

        return pd.DataFrame(activities)