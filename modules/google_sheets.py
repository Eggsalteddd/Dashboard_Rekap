import pandas as pd

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from streamlit import cache_resource, cache_data

from config.config import (
    SCOPES,
    GOOGLE_CREDENTIALS,
    SPREADSHEET_ID,
    RANGE_NAME
)


@cache_resource
def connect_google_sheets():

    creds = Credentials.from_service_account_info(
       GOOGLE_CREDENTIALS,
        scopes=SCOPES
    )

    service = build(
        "sheets",
        "v4",
        credentials=creds
    )

    return service


@cache_data(ttl=30)
def get_data():

    service = connect_google_sheets()

    result = (
        service
        .spreadsheets()
        .values()
        .get(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE_NAME
        )
        .execute()
    )

    rows = result.get("values", [])

    if not rows:
        return pd.DataFrame()

    columns = [
        "Kode_SubSLS",
        "Nama_SLS",
        "C",
        "D",
        "PPL",
        "F",
        "G",
        "H",
        "TOTAL",
        "OPEN",
        "SUBMIT",
        "REJECT",
        "APPROVE",
        "PERSEN",
        "O",
        "PERSEN_PML",
        "Q",
        "R",
        "PENGECEKAN",
        "CATATAN"
    ]

    normalized_rows = []

    for row in rows[1:]:

        row = row + [""] * (20 - len(row))

        normalized_rows.append(
            row[:20]
        )

    df = pd.DataFrame(
        normalized_rows,
        columns=columns
    )

    return df