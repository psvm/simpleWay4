#Replace 2 column with max and min numbers of even elements in matrix [m x n]
import random


def replace_min_max_even_number_column(element, number_of_rows, number_of_column):
    even_count = []
    index_max_even_column = None
    index_min_even_column = None
    list_for_calculating = []
    for j in range(0, number_of_column):
        for i in range(0, number_of_rows):
            list_for_calculating.append(element[i][j])
        even_count.append(len(list(filter(lambda x: x % 2 == 0, list_for_calculating[:]))))
        list_for_calculating.clear()
        index_max_even_column = even_count.index(max(even_count))
        index_min_even_column = even_count.index(min(even_count))

    print("")
    for i in range(0, number_of_rows):
        temp_var = element[i][index_min_even_column]
        element[i][index_min_even_column] = element[i][index_max_even_column]
        element[i][index_max_even_column] = temp_var


element = []
number_of_rows = 5
number_of_column = 7
row = []
new_element = []
for i in range(0, number_of_rows):
    for j in range(0, number_of_column):
        row.append(random.randint(1, 9))
    element.append(row[0: number_of_column])
    row.clear()

for i in element:
    print(i)

replace_min_max_even_number_column(element, number_of_rows, number_of_column)

print("")

for i in element:
    print(i)
