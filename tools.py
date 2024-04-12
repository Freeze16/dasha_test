import csv
import typing as t

from .config import PARTICIPANTS_RAW_CSV


def get_participants_emails() -> t.List[dict]:
    with open(PARTICIPANTS_RAW_CSV) as csvfile:
        reader = csv.DictReader(csvfile)
        return [row["E-mail:"] for row in reader]