import csv
import re
from pathlib import Path
from datetime import date

RAW_SLEEP_PATH = Path("data/raw/garmin/sleep")
OUTPUT_PATH = Path("data/bronze/garmin/sleep")

OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def parse_duration_to_minutes(duration_str: str) -> int | None:
    """
    Converte '4h 5min' -> 245
    Retorna None se vazio ou inválido
    """
    if not duration_str or duration_str.strip() in {"--", ""}:
        return None

    hours = 0
    minutes = 0

    h_match = re.search(r"(\d+)h", duration_str)
    m_match = re.search(r"(\d+)min", duration_str)

    if h_match:
        hours = int(h_match.group(1))
    if m_match:
        minutes = int(m_match.group(1))

    return hours * 60 + minutes


def load_sleep_csvs():
    records = []
    ingestion_date = date.today().isoformat()

    for csv_file in RAW_SLEEP_PATH.glob("*.csv"):
        with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                sleep_date = list(row.values())[0]
                duration_raw = list(row.values())[1]
                sleep_start = list(row.values())[2]
                sleep_end = list(row.values())[3]

                record = {
                    "sleep_date": sleep_date,
                    "sleep_duration_min": parse_duration_to_minutes(duration_raw),
                    "sleep_start_time": sleep_start,
                    "sleep_end_time": sleep_end,
                    "source_file": csv_file.name,
                    "ingestion_date": ingestion_date,
                }

                records.append(record)

    return records


def write_bronze_sleep(records):
    output_file = OUTPUT_PATH / "sleep_bronze.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = records[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(records)


if __name__ == "__main__":
    sleep_records = load_sleep_csvs()

    if not sleep_records:
        print("Nenhum dado de sono encontrado.")
    else:
        write_bronze_sleep(sleep_records)
        print(f"{len(sleep_records)} registros de sono processados com sucesso.")
