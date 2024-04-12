import os

from dotenv import load_dotenv

load_dotenv()

DASHA_API_KEY = os.getenv("DASHA_API_KEY")
DASHA_BASE_ID = os.getenv("DASHA_BASE_ID")

PARTICIPANTS_RAW_CSV = os.getenv("PARTICIPANTS_RAW_CSV")
