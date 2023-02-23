import random
import numpy as np
mas = []
m = random.randint(3, 4) #задание диапазона размеров квадратной матрицы
matr = np.random.randint(0, 20, (m, m))#задание диапазона значений переменных в матрице
print(matr)
arr2 = np.rot90(matr) #отражение матрицы по оси х(становление побочной диагонали главной)
arr1 = np.prod(np.diag(arr2, 1)) #перемножение элементов идущих в данный момент над главной диагональю
arr4 = np.prod(np.diag(arr2, -1)) #перемножение элементов идущих в данный момент под главной диагональю
print(arr1)
print(arr4)
mas.append(arr1)
mas.append(arr4)
for i in range(1, m):
    mas.append(" ")
del (mas[-1])
new_row = np.array(mas)#создание строки из значений arr1 и arr4
matr = np.vstack([matr, new_row])#последовательный вывод матрицы и вывод на новой строке значений перемноженных чисел
np.savetxt('test.txt', matr, fmt="%.18s")#вывод значений в файл




