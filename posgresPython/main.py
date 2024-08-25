import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def process_data(engine):
    conn = engine.connect()

    data = pd.read_sql("select name, min(age) as min_age, max(age) as max_age from test_table where length(name) < 6 group by name", conn)
    return data


if __name__ == "__main__":
    db_user = 'postgres'
    db_password = 'password'
    db_host = 'db'
    db_port = '5432'
    db_name = 'kuntsev_db'

    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    result = process_data(engine)
    
    print("Максимальный и минимальный возраст для имен, длина которых меньше 6 символов:")

    print(result)


