import streamlit as st


def show_table(df):

    st.subheader("📑 Detail Data")

    display_df = df[
        [
            "Kode_SubSLS",
            "Nama_SLS",
            "PPL",
            "TOTAL",
            "OPEN",
            "SUBMIT",
            "REJECT",
            "APPROVE",
            "PERSEN",
            "PERSEN_PML",
            "PENGECEKAN",
            "CATATAN"
        ]
    ].copy()

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,

        column_config={

            "Kode_SubSLS":
                st.column_config.TextColumn(
                    "Kode SubSLS"
                ),

            "Nama_SLS":
                st.column_config.TextColumn(
                    "Nama SLS"
                ),

            "PPL":
                st.column_config.TextColumn(
                    "PPL"
                ),

            "TOTAL":
                st.column_config.NumberColumn(
                    "TOTAL"
                ),

            "OPEN":
                st.column_config.NumberColumn(
                    "OPEN"
                ),

            "SUBMIT":
                st.column_config.NumberColumn(
                    "SUBMIT"
                ),

            "REJECT":
                st.column_config.NumberColumn(
                    "REJECT"
                ),

            "APPROVE":
                st.column_config.NumberColumn(
                    "APPROVE"
                ),

            "PERSEN":
                st.column_config.TextColumn(
                    "PERSEN"
                ),

            "PERSEN_PML":
                st.column_config.TextColumn(
                    "PERSEN PML"
                ),

            "PENGECEKAN":
                st.column_config.CheckboxColumn(
                    "Pengecekan"
                ),

            "CATATAN":
                st.column_config.TextColumn(
                    "Catatan"
                )
        }
    )