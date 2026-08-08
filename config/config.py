import streamlit as st

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

SPREADSHEET_ID = "1jNWOPMfGkxy2AopklZYc6HLFujN42UbAHLBpIqMv_wY"

RANGE_NAME = "Produktivitas!A1:T53"

GOOGLE_CREDENTIALS = st.secrets["gcp_service_account"]