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
df = pd.read_sql('SELECT * FROM SRV.EstoqueProdutos', sqlserver_conn)
print(f'Total: {len(df)} registros')

# evitar duplicidade (opcional)
ids_mysql = pd.read_sql('SELECT IdEstoqueProduto FROM EstoqueProdutos', mysql_conn)
df = df[~df['IdEstoqueProduto'].isin(ids_mysql['IdEstoqueProduto'])]

print(f'Novos registros: {len(df)}')

df.rename(columns={'IdOrgao': 'IdEntidade'}, inplace=True)

# envio
df.to_sql(
    'estoqueprodutos',
    con=mysql_conn,
    if_exists='append',
    index=False,
    chunksize=1000,
    method='multi'
)

print('🚀 Migração finalizada!')