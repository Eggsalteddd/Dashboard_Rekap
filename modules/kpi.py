import streamlit as st


def show_kpi(df):

    total_sls = len(df)

    total_target = df["TOTAL"].sum()
    total_open = df["OPEN"].sum()
    total_submit = df["SUBMIT"].sum()
    total_reject = df["REJECT"].sum()
    total_approve = df["APPROVE"].sum()

    if total_target > 0:

        overall_progress = (
            total_submit
            + total_reject
            + total_approve
        ) / total_target

    else:

        overall_progress = 0

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric(
        "📍 Total SLS",
        f"{total_sls:,}"
    )

    col2.metric(
        "🎯 TOTAL",
        f"{total_target:,}"
    )

    col3.metric(
        "🟡 OPEN",
        f"{total_open:,}"
    )

    col4.metric(
        "🔵 SUBMIT",
        f"{total_submit:,}"
    )

    col5.metric(
        "🔴 REJECT",
        f"{total_reject:,}"
    )

    col6.metric(
        "🟢 APPROVE",
        f"{total_approve:,}"
    )

    return overall_progress