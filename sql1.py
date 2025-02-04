import pandas as pd
import numpy as np
from sqlalchemy import create_engine
username = 'root'
password = '1234'
host = 'localhost'
database = 'teju'
connection_string = f'mysql+mysqlconnector://{username}:{password}@{host}/{database}'
engine = create_engine(connection_string)
df_candidates = pd.read_sql('SELECT * FROM Candidates', engine)

csv_file_path = "C:/6654_project/jobs_data.csv"
df_jobs = pd.read_csv(csv_file_path)
print(df_candidates['Age'].dtypes)
df_merged = pd.merge(df_candidates, df_jobs, on="CandidateID",how='inner')
print(f"Memory Usage: {df_candidates.memory_usage(deep=True)}")
df_candidates['Age'] = df_candidates['Age'].astype(np.int16)
print(f"Memory Usage: {df_candidates.memory_usage(deep=True)}")
print(df_candidates['Age'].dtypes)
print(df_merged)

#df_merged.to_excel("merged_data.xlsx", index=False)