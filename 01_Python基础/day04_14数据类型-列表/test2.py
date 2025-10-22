items = [('apple', 2.5), ('banana', 1.8), ('orange', 3.0), ('grape', 2.8)]
temp_list = []
for name, price in items:
    temp_list.append((price, name))
sorted_temp = sorted(temp_list)
sorted_items = []
for price, name in sorted_temp:
    sorted_items.append((name, price))

print(sorted_items)