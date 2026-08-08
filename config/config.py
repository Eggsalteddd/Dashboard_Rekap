import os

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

SERVICE_ACCOUNT_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "credentials",
    "service_account.json"
)

SPREADSHEET_ID = (
    "1jNWOPMfGkxy2AopklZYc6HLFujN42UbAHLBpIqMv_wY"
)

RANGE_NAME = "Produktivitas!A1:T53"