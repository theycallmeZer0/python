import random
import sys
mas = []
masnew = []
def sortndelete(mas): #функция без использования упрощенных методов(1)
    n = 0
    j = 0
    masnew = []
    print("Новый массив")
    for m in range(0, len(mas)):
        if mas[m] % 2 == 0:
            masnew += [int(mas[m])] #добавление в новый мкассив всех четных элеметов
        elif mas[m] % 2 == 1:
            n = mas[m] #присвоение переменной n значение нечетного элемента
            for i in range(0, len(mas)):
                if n == mas[i]: #поддсчет кол-ва совпадений осташихся элементов с переменной n
                    j += 1
            if j > 1:
                masnew += [int(n)] #вывод нечетных элементов встречающихся больше 1 раза в массиве
            j = 0
    print(masnew)
def sortdel(mas): #функция с упрощенными методами(2)
    print("Новый массив")
    for i in range(0, len(mas)):
        masnew.append(mas.count(mas[i])) #подсчет кол-ва вхождений чисесл в массив
    for i in range(0, len(masnew)):
        if masnew[i] == 1 and mas[i] % 2 != 0: #удаление элементова подходящих под условия задачи
            mas[i] = " "
while True:
    a = int(input("Веедите 1 для автоматического заполнения или 2 для руного ввода: "))
    if a == 1:
        mas = [random.randint(0, 100) for i in range(random.randint(5, 10))]
        print("Исходный массив")
        print(mas)
        sortndelete(mas) #вызов функции 1
    elif a == 2:
        count = int(input("Введите желаемое количество элементов массива: "))
        for i in range(count):
            mas.append(int(input()))
        print("Исходный массив")
        sortdel(mas) #вызов функци 2
        g = 0
        while " " in mas: # удаление пустот от удаленных элементов
            if mas[g] == " ":
                del mas[g]
            g += 1
        print(mas)
    else: #сообщение об ошибке ввода
        print("Input error")
        sys.exit()