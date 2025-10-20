# Write a Pandas program to drop rows with missing data.

import pandas as pd

a = {
    'Name': ['Saim', 'Haider', 'Zaeem', 'Fahad'],
    'Age': [None, 21, None, 31],
    'City': ['Bahawalpur', 'Kashmir', None, 'Lahore']
}

b = pd.DataFrame(a)

b_dropped = b.dropna()
print(b_dropped)

