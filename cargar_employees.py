import pandas as pd
import numpy as np

def read_csv(file_name):
    CSV_URL=f"C:/Users/Asus/OneDrive/Documentos/Entrevistas/Globant/Challenge_DA/{file_name}.csv"

    # Leer CSV con pandas
    df_pandas = pd.read_csv(CSV_URL, sep=',', header = None)

    return df_pandas

def clean_data(df):
    #nan_rows = df[df.isnull().any(1)]
    df = df.fillna(value=np.nan)
    df = df.dropna()
    return df
