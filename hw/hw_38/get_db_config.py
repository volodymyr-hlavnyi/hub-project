import dotenv
import os
from Connector import Connector


def get_db_config():
    dotenv.load_dotenv()
    ICH_HOST = os.getenv("ICH_HOST")
    ICH_PASSWORD = os.getenv("ICH_PASSWORD")
    ICH_USER = os.getenv("ICH_USER")
    ICH_DATABASE = os.getenv("ICH_DATABASE")

    dbconfig = {
        'host': f"{ICH_HOST}",
        'user': f"{ICH_USER}",
        'password': f"{ICH_PASSWORD}",
        'database': f"{ICH_DATABASE}",
    }

    return dbconfig
