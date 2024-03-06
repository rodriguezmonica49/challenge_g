import pandas as pd



def read_csv(file_name,columns):
    CSV_URL=f"C:/Users/Asus/OneDrive/Documentos/Entrevistas/Globant/Challenge_DA/{file_name}.csv"

    # Leer CSV con pandas
    df_pandas = pd.read_csv(CSV_URL, sep=',',usecols=columns)

    return df_pandas

#def insert_sql(df, name_table):


df_employees = read_csv("hired_employees",['index','campo1','campo2','campo3','campo4'])
#df_departments = read_csv("departments",[])
#df_jobs = read_csv("jobs",[])


