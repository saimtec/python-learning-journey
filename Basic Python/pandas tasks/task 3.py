#  Data Cleaning Techniques

# Write a Pandas program to detect duplicates using duplicated() method.

import pandas as pd
a = pd.DataFrame({
    'ID': [1, 2, 2, 3, 4, 4],
  'Name': ['Saim', 'Haider', 'Haider', 'Fahad', 'Noman', 'Noman']
})


dup_check = a.duplicated()
print("Duplicate rows: ")
print(a[dup_check])
