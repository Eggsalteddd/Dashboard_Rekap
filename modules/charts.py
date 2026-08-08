import streamlit as st
import pandas as pd
import plotly.express as px


def show_progress_chart(df):

    st.subheader("📊 Progress per SLS")

    chart_df = df.copy()

    chart_df["Progress"] = (
        chart_df["PERSEN_VALUE"] * 100
    )

    fig = px.bar(
        chart_df.sort_values(
            "Progress",
            ascending=True
        ),
        x="Progress",
        y="Nama_SLS",
        color="Progress",
        orientation="h",
        text="Progress",
        color_continuous_scale=[
            "#d73027",
            "#fc8d59",
            "#fee08b",
            "#91cf60",
            "#1a9850"
        ]
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Progress (%)",
        yaxis_title="SLS",
        xaxis_range=[0, 110],
        height=max(
            400,
            len(chart_df) * 35
        ),
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_status_chart(df):

    st.subheader("📋 Status Pendataan")

    status_data = pd.DataFrame({
        "Status": [
            "OPEN",
            "SUBMIT",
            "REJECT",
            "APPROVE"
        ],
        "Jumlah": [
            df["OPEN"].sum(),
            df["SUBMIT"].sum(),
            df["REJECT"].sum(),
            df["APPROVE"].sum()
        ]
    })

    fig = px.bar(
        status_data,
        x="Status",
        y="Jumlah",
        color="Status",
        text="Jumlah",
        color_discrete_map={
            "OPEN": "#f39c12",
            "SUBMIT": "#3498db",
            "REJECT": "#e74c3c",
            "APPROVE": "#2ecc71"
        }
    )

    fig.update_traces(
        textposition="outside"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


def show_ppl_chart(df):

    st.subheader("👤 Progress berdasarkan PPL")

    summary = (
        df
        .groupby("PPL")
        .agg(
            TOTAL=("TOTAL", "sum"),
            SUBMIT=("SUBMIT", "sum"),
            REJECT=("REJECT", "sum"),
            APPROVE=("APPROVE", "sum")
        )
        .reset_index()
    )

    summary["Progress"] = (
        (
            summary["SUBMIT"]
            + summary["REJECT"]
            + summary["APPROVE"]
        )
        /
        summary["TOTAL"].replace(
            0,
            pd.NA
        )
    ).fillna(0) * 100

    fig = px.bar(
        summary.sort_values(
            "Progress",
            ascending=False
        ),
        x="PPL",
        y="Progress",
        color="Progress",
        text="Progress",
        color_continuous_scale="Blues"
    )

    fig.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside"
    )

    fig.update_layout(
        yaxis_title="Progress (%)",
        xaxis_title="PPL",
        yaxis_range=[0, 110],
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )