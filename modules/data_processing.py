import pandas as pd


def clean_data(df):

    df = df.copy()

    numeric_columns = [
        "TOTAL",
        "OPEN",
        "SUBMIT",
        "REJECT",
        "APPROVE"
    ]

    for col in numeric_columns:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        ).fillna(0)

    # Progress
    df["PERSEN_VALUE"] = (
        (
            df["SUBMIT"]
            + df["REJECT"]
            + df["APPROVE"]
        )
        /
        df["TOTAL"].replace(0, pd.NA)
    )

    df["PERSEN_VALUE"] = (
        df["PERSEN_VALUE"]
        .fillna(0)
    )

    # PERSEN PML
    df["PERSEN_PML_VALUE"] = (
        df["PERSEN_PML"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["PERSEN_PML_VALUE"] = pd.to_numeric(
        df["PERSEN_PML_VALUE"],
        errors="coerce"
    ).fillna(0) / 100

    # Extract RW
    df["RW"] = (
        df["Nama_SLS"]
        .astype(str)
        .str.extract(r"(RW\s*\d+)")[0]
    )

    return df