from sqlalchemy import create_engine
from sqlalchemy.engine import URL

def get_engine():
    url = URL.create(
        drivername='mysql+pymysql',
        username='root',
        password='@SRVtag2532',
        host='localhost',
        database='vipsgs_db'
    )

    engine = create_engine(url)
    return engine