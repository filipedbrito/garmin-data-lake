from ingestion.garmin_api import get_daily_wellness
import json

if __name__ == "__main__":
    data = get_daily_wellness("2026-01-28")
    print(json.dumps(data, indent=2, ensure_ascii=False))
