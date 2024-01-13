# %%
import os
import pandas as pd

SPREADSHEETS_DIR = "./spreadsheets/"
STATEMENTS_DIR = f"{SPREADSHEETS_DIR}/yahav_statements"
CREDIT_CARDS_DIR = f"{SPREADSHEETS_DIR}/yahav_credit_card"

def read_bank_statements() -> pd.DataFrame:
    """Reads the bank statements from the bank statements directory and returns dataframe"""
    dfs = []
    for item in os.listdir(STATEMENTS_DIR):
        df = pd.read_excel(f"{STATEMENTS_DIR}/{item}", skiprows=range(4))
        columns = [
            "date",
            "date_value",
            "transaction_num",
            "description",
            "debit",
            "credit",
            "estimated_balance",
        ]
        df.rename(
            columns={original: new for original, new in zip(df.columns, columns)},
            inplace=True,
        )
        dfs.append(df)
    return pd.concat(dfs, join="inner")


def read_credit_statements() -> pd.DataFrame:
    """Reads the credit card statements from the credit card statements directory
    returns a dataframe"""
    dfs = []
    for item in os.listdir(CREDIT_CARDS_DIR):
        df = pd.read_excel(f"{CREDIT_CARDS_DIR}/{item}", skiprows=range(8))
        drop_list = [column for column in df.columns if df[column].count() == 0]
        df.drop(columns=drop_list, inplace=True)
        dfs.append(df)
    return pd.concat(dfs)
        

df = read_credit_statements()

# %%
df
# %%
