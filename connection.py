from sqlalchemy import create_engine, MetaData, Table, select
ServerName = "DESKTOP-M804PST"
Database = "Globant"
TableName = "mytable"

import pyodbc
from cargar_employees import df_employees

print(pyodbc.drivers())

driver = "ODBC+Driver+17+for+SQL+Server"

#engine = create_engine(f'mssql+pyodbc://{ServerName}/{Database}?driver={driver}? Trusted_Connection=yes')
#engine = create_engine('mssql://' + ServerName + '/' + Database)
engine = create_engine("mssql+pyodbc://sa:12345678@ODBCLocal",fast_executemany=True)
conn = engine.connect()
print(conn)
#metadata = MetaData(conn)

df_employees.to_sql(TableName, engine, chunksize=419,index=False, method='multi',if_exists='replace')
