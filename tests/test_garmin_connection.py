from ingestion.garmin_client import get_garmin_client

if __name__ == "__main__":
    client = get_garmin_client()
    print(dir(client))