"""
Day 10 Activity: Outliers Practice
Tasks:
1) Implement IQR-based outlier detection
2) Implement z-score detection
3) Compare strategies: no handling, IQR capping, log1p transform
"""

import numpy as np
import pandas as pd

# Sample heavy-tailed data


df = pd.read_csv("day10_outliers.csv")

# TODO: Implement iqr_bounds and detect_outliers_iqr
def iqr_bounds(s, k=1.5):
    q1, q3 = s.quantile(0.25), s.quantile(0.75)
    iqr=q3-q1
    return q1-k*iqr, q3+k*iqr
lower, upper = iqr_bounds(df["income"], k=1.5)
mask_iqr = (df["income"]<lower) | (df["income"]>upper)
print(~mask_iqr)


# TODO: Implement detect_outliers_zscore
income=df["income"].astype(float)
mean, std=income.mean(), income.std(ddof=0)

df["income_z"]=(income-mean)/std
mask_z=df["income_z"].abs()>3
print("Z-score outlaiers:\n", df[mask_z])


# TODO: Apply capping and log1p transformation
df_capped=df.copy()
df_capped["income_capped"]=df_capped["income"].clip(lower=lower, upper=upper)
df_trans=df.copy()
df_trans["income_loglp"]=np.log1p(df_trans["income"])