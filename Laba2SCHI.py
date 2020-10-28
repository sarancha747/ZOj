import numpy as np
from PIL import Image

img = Image.open('image.bmp')
arr = np.asarray(img, dtype='uint8')
work_array = [[1]*40]*40
print(work_array)
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j][1] < 200:
            work_array[i][j] = 0
            #print(i, j, arr[i][j][1], work_array[i][j])
            print(work_array[i][j], end=' ')
        else:

            work_array[i][j] = 1
            #print(i, j, arr[i][j][1], work_array[i][j])
            print(work_array[i][j], end=' ')
    print()
print(len(work_array))
#for i in range(len(work_array)):
#    for j in range(len(work_array[i])):
#        print(work_array[i][j], end=' ')
#    print()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(work_array[i][j], end=' ')
    print()

print(arr)
