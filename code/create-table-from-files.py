import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('/home/informatics/de15_project3/source/users_w_postal_code.csv', sep=',')
engine = create_engine('postgresql://postgres:digitalskola@127.0.0.1:5432/postgres')

df.to_sql("from_file_table",engine, if_exists='replace')
df_read = pd.read_sql("SELECT * FROM from_file_table",engine)
print(df_read.head())