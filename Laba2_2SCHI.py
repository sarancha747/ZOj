import numpy as np
from PIL import Image

img = Image.open('image.bmp')
arr = np.asarray(img, dtype='uint8') #завантажуємо і перетворюємо зображення в двомірний масив

work_array = []

for i in range(len(arr)):#перетворюємо з rgb в 0 і 1
    row = []
    for j in range(len(arr[i])):
        if arr[i][j][1] < 200:
            row.append(1)
        else:
            row.append(0)
    work_array.append(row)

for i in range(len(work_array)): #виводимо масив
    for j in range(len(work_array[i])):
        print(work_array[i][j], end=' ')
    print()

print('##########################')

for i in range(len(work_array)):#заміняємо контур на двійку
    for j in range(len(work_array[i])):
        if work_array[i][j] == 1:
            if   i != 0 and work_array[i - 1][j] == 0:#зверху
                work_array[i - 1][j] = 2

            if j != 39 and work_array[i][j + 1] == 0:#зправа
                work_array[i][j + 1] = 2

            if i != 39 and work_array[i + 1][j] == 0:#знизу
                work_array[i + 1][j] = 2
            if j != 0 and work_array[i][j - 1] == 0:#зліва
                work_array[i][j - 1] = 2

for i in range(len(work_array)):#виводимо масив
    for j in range(len(work_array[i])):
        print(work_array[i][j], end=' ')
    print()

print('##########################')

for i in range(len(work_array)):#заміняємо 2 на 1 і все інше на 0
    for j in range(len(work_array[i])):
        if work_array[i][j] == 2:
            work_array[i][j] = 1
        else:
            work_array[i][j] = 0

for i in range(len(work_array)):#виводимо масив
    for j in range(len(work_array[i])):
        print(work_array[i][j], end=' ')
    print()

print('##########################')

comp_arr = []
for i in range(len(work_array)):#заміняємо 2 на 1 1 1  а 0 на 255 255 255 RGB
    row = []
    for j in range(len(work_array[i])):
        if work_array[i][j] == 1:
            row.append([1,1,1])
        else:
            row.append([255,255,255])
    comp_arr.append(row)

print(comp_arr)
arr = np.array(comp_arr, dtype='uint8')#створюємо зображення
img = Image.fromarray(arr, 'RGB')
img.save('my.bmp')
