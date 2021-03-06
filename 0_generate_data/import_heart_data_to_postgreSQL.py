import numpy as np
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql

from sqlalchemy import create_engine

engine = create_engine(r'postgresql+psycopg2://postgres:xxx@localhost:5432/heart_dataset_random_same_column')

conn = pg.connect("dbname=heart user=postgres password=xxx")
df = psql.read_sql("SELECT * FROM heart_disease", conn)

# read the file and create a pandas dataframe

#Export to postgre
print("exporting to postgre table")
c = engine.connect()
conn = c.connection
df.to_sql('heart', engine)

conn.close()

