# Handling Missing Data in Pandas

# Write a Pandas program to fill missing values (NaN) in a DataFrame using fillna().



import pandas as pd

a = {
    'Name': ['Saim', 'Haider', 'Zaeem', 'Fahad'],
    'Age': [None, 21, None, 31],
    'City': ['Bahawalpur', 'Kashmir', None, 'Lahore']
}

b = pd.DataFrame(a)

# Fill missing values
b_filled = b.fillna({
    'Age': b['Age'].mean(),  
    'City': 'Karachi'
})

print(b_filled)
