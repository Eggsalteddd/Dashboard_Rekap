import streamlit as st

from modules.google_sheets import get_data
from modules.data_processing import clean_data
from modules.filters import show_filters, apply_filters
from modules.kpi import show_kpi
from modules.charts import show_progress_chart
from modules.charts import show_status_chart
from modules.charts import show_ppl_chart
from modules.table import show_table


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Dashboard Rekap",
    page_icon="📊",
    layout="wide"
)


# =========================
# LOAD DATA
# =========================

df = get_data()

if df.empty:
    st.warning("Data tidak ditemukan.")
    st.stop()


# =========================
# CLEAN DATA
# =========================

df = clean_data(df)


# =========================
# FILTER
# =========================

selected_ppl, selected_rw, selected_sls = show_filters(df)

df_filtered = apply_filters(
    df,
    selected_ppl,
    selected_rw,
    selected_sls
)

# =========================
# TITLE
# =========================

st.title("📊 Dashboard Rekap")
st.markdown("---")


# =========================
# KPI
# =========================

show_kpi(df_filtered)

# =========================
# TABLE
# =========================

show_table(df_filtered)

# =========================
# CHARTS
# =========================

show_progress_chart(df_filtered)

show_status_chart(df_filtered)

show_ppl_chart(df_filtered)


