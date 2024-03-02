import time

import requests

from .config.settings import Config
from .services.adverse_incidents import AdverseIncidentsService


def get_incidents():
    adverse_incidents_service = AdverseIncidentsService()
    while True:
        try:
            response = requests.get(Config.ADVERSE_INCIDENTS_PROVIDER_URL,
                                    headers={"x-api-key": Config.ADVERSE_INCIDENTS_PROVIDER_API_KEY})
            if response.status_code == 200:
                incidents = response.json()
                adverse_incidents_service.process_adverse_incidents(incidents)
            else:
                print(f"Error: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print(
                f"Waiting {Config.ADVERSE_INCIDENTS_PROVIDER_REFRESH_INTERVAL_SECONDS} seconds to get the next incidents...")
            time.sleep(Config.ADVERSE_INCIDENTS_PROVIDER_REFRESH_INTERVAL_SECONDS)


if __name__ == "__main__":
    get_incidents()
