import duckdb
import pandas as pd
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config.database import get_sqlserver_engine, get_mysql_engine

# con = duckdb.connect(database='teste', read_only=False)

# conexões
sqlserver_conn = get_sqlserver_engine()
mysql_conn = get_mysql_engine()

# teste
with sqlserver_conn.connect() as conn:
    print('✅ SQL Server OK')

with mysql_conn.connect() as conn:
    print('✅ MySQL OK')

# leitura
df = pd.read_sql('select * from SRV.Produtos', sqlserver_conn)
print(f'Total: {len(df)} registros')


# envio
df.to_sql('produtos', con=mysql_conn, if_exists='append', index=False)
print('🚀 Migração finalizada!')