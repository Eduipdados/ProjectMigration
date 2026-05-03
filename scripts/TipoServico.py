import duckdb
import pandas as pd
import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from config.database import get_engine

# con = duckdb.connect(database='teste', read_only=False)

engine = get_engine()

# Teste (opcional)
with engine.connect() as conn:
    print('✅ Conectado!')

# Caminho do CSV
caminho_csv = 'landing/tiposservicos.csv'

df = pd.read_csv(
    caminho_csv,
    sep=';',
    encoding='utf-8',
    quotechar='"',
    na_values=['NULL']
)

df.to_sql('tiposervicos', con=engine, if_exists='append', index=False)

print(f'✅ {len(df)} registros importados com sucesso!')