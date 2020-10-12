import csv
import numpy

#reader = csv.reader(open("dara.csv", "r", encoding="UTF-8"), delimiter=",")
#reader = csv.reader(open("dara2.csv", "r", encoding="UTF-8"), delimiter=",")
reader = csv.reader(open("dara3.csv", "r", encoding="UTF-8"), delimiter=",")
x = list(reader)
matrix = numpy.array(x).astype("int")  # створення масиву з файлу

start = 15  # задаємо вершину старту
stop = 12  # задаємо вершину кінця

size = 16  # задаємо кількість вершин в графі
steck = [start]  # стек для зберігання вершин
position = start - 1  # створюємо позицію першої вершини
path_found = False


def finder(position, previous_row, previous_column):
    global path_found
    for i in range(len(matrix[position])):  # проходимо по всім елементам рядка матриці
        if position == stop - 1 or path_found == True:  # якщо ми знайшли останній елемент то закінчити всі функції в рекурсії
            print("stop")
            path_found = True
            return 1
        elif matrix[position][i] == 1:  # якщо заноходимо звязок то додаємо вершину до стеку
            print(i)
            steck.append(i + 1)
            matrix[previous_row][previous_column] = 0
            finder(i, position, i)
        elif matrix[position][i] == 0 and i == size - 1:  # якщо остання вершина = 0 то виходимо з рекурсії і
            print("back")
            matrix[previous_row][previous_column] = 0
            steck.pop()
            # return 1


finder(position, 0, 0)

if path_found:
    print(steck)
else:
    print("\nШлях не знайдено ")
