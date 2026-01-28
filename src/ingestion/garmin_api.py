from typing import Dict
from ingestion.garmin_client import get_garmin_client


def get_daily_wellness(date: str) -> Dict:
    """
    Busca métricas diárias de wellness do Garmin.
    Exemplo de date: '2026-01-28'
    """
    client = get_garmin_client()

    response = client.get(
        "connectapi",
        f"/wellness-service/wellness/daily/{date}"
    )

    return response