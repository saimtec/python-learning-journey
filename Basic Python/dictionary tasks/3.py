# 3.Get Top Three Items in a Shop

# Write a Python program to get the top three items in a shop.

# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3


from heapq import nlargest
from operator import itemgetter

items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

top_items = nlargest(3, items.items(), key=itemgetter(1))

for name, value in top_items:
    print(name, value)
