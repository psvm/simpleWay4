import random

number_of_rows = 5
number_of_column = 10
element = []
row = []
even_count = []
for i in range(0, number_of_rows):
    for j in range (0, number_of_column):
        row.append(random.randint(0,10))
    element.append(row[0: number_of_column])
    row.clear()
for i in range(0, number_of_rows):
    even_count.append(len(list(filter(lambda x: x%2 == 0, element[:][i]))))
print(element)
print(even_count)

