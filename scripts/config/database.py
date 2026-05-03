from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# 🔵 MySQL
def get_mysql_engine():
    url = URL.create(
        drivername='mysql+pymysql',
        username='root',
        password='@SRVtag2532',
        host='localhost',
        database='vipsgs_db'
    )

    return create_engine(url)


# 🔵 SQL Server (Windows Authentication)
def get_sqlserver_engine():
    connection_string = (
        "mssql+pyodbc://@localhost/DbVipsgs"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&Trusted_Connection=yes"
    )

    return create_engine(connection_string)