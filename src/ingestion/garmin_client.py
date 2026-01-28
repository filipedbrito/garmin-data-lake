import os
from dotenv import load_dotenv
from garth import Client


def get_garmin_client() -> Client:
    """
    Cria e autentiva um cliente do garmin connect usando as credenciais do .env
    Essa função retorna um objeto do tipo Client
    """
    load_dotenv()

    email = os.getenv("GARMIN_EMAIL")
    password = os.getenv("GARMIN_PASSWORD")

    if not email or not password:
        raise ValueError("Credenciais do garmin connect não encontradas no .env")
    
    client = Client()
    client.login(email, password)

    return client