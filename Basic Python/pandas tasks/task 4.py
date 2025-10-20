# 4. String Manipulation in Pandas

# Write a Pandas program to remove duplicates rows from a DataFrame.


import pandas as pd
a = pd.DataFrame({
    'ID': [1, 2, 2, 3, 4, 4],
  'Name': ['Saim', 'Haider', 'Haider', 'Fahad', 'Noman', 'Noman']
})

drop_dup = a.drop_duplicates()
print("After removing duplicate rows : ")
print(drop_dup)


