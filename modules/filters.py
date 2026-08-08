import streamlit as st


def show_filters(df):

    st.sidebar.title("🔎 Filter")

    # -------------------------
    # PPL
    # -------------------------

    ppl_options = sorted(
        df["PPL"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_ppl = st.sidebar.multiselect(
        "PPL",
        ppl_options
    )

    # -------------------------
    # RW
    # -------------------------

    rw_options = sorted(
        df["RW"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_rw = st.sidebar.multiselect(
        "RW",
        rw_options
    )

    # -------------------------
    # SLS
    # -------------------------

    sls_options = sorted(
        df["Nama_SLS"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_sls = st.sidebar.multiselect(
        "SLS",
        sls_options
    )

    return (
        selected_ppl,
        selected_rw,
        selected_sls
    )


def apply_filters(
    df,
    selected_ppl,
    selected_rw,
    selected_sls
):

    filtered_df = df.copy()

    if selected_ppl:

        filtered_df = filtered_df[
            filtered_df["PPL"].isin(
                selected_ppl
            )
        ]

    if selected_rw:

        filtered_df = filtered_df[
            filtered_df["RW"].isin(
                selected_rw
            )
        ]

    if selected_sls:

        filtered_df = filtered_df[
            filtered_df["Nama_SLS"].isin(
                selected_sls
            )
        ]

    return filtered_df