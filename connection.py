from sqlalchemy import create_engine

driver = "ODBC+Driver+17+for+SQL+Server"

engine = create_engine("mssql+pyodbc://sa:12345678@ODBCLocal",fast_executemany=True)
engine.connect()
