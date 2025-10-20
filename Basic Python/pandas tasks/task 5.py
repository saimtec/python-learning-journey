# 5. Handling Outliers with Z-Score Method

# Write a Pandas program to handle outliers in a DataFrame with Z-Score method.


import pandas as pd

abx = pd.DataFrame({
    'Score': [100, 105, 98, 102, 1000, 101, 99]  
})

mean = abx['Score'].mean()
std = abx['Score'].std()

abx['Z_score'] = (abx['Score'] - mean) / std

threshold = 2
abx_no_outliers = abx[abx['Z_score'].abs() < threshold]

print("Original DataFrame with Z-scores:")
print(abx)

print("\nDataFrame without outliers:")
print(abx_no_outliers)
