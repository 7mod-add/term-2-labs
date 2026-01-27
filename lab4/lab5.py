import numpy as np
import pandas as pd

df=pd.read_csv("day06_user_data.csv")
print(df)
custom_missing=["N/a", "NA", "not reported", "unknown", "?"]
df_norm = df.copy()
df_norm=df_norm.replace(custom_missing, np.nan)
print(df_norm)

df_imp=df_norm.copy()
df_imp["income"]=pd.to_numeric(df_imp["income"], errors="coerce")
df_imp["age"]=pd.to_numeric(df_imp["age"], errors="coerce")

df_imp["income"]=df_imp["income"].fillna(df_imp["income"].median())
df_imp["age"]=df_imp["age"].fillna(df_imp["age"].mean())

mode_city=df_imp["city"].mode(dropna=True)[0]
df_imp["city"]=df_imp["city"].fillna(mode_city)

print(df_imp)