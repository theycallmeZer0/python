import csv
import pathlib
from pathlib import Path


def count():
    name = input("Enter folder name: ")
    folder = Path(name)
    if folder.is_dir():
        count = len([1 for file in folder.iterdir()])
    print(f"In this folder there are {count} folders or files")

def write_csv(dictionary):
    key_inp = input('Enter ID: ')
    date1_inp = input('Enter date and time of begin: ')
    date2_inp = input('Enter date and time of end: ')
    phone_inp = input('Enter phone number: ')
    distance_inp = input('Enter distance: ')
    price_inp = input('Enter price: ')
    dictionary[key_inp] = [date1_inp, date2_inp, phone_inp, distance_inp, price_inp]#создание словаря
    with open('data.csv', 'w') as f:
        for elem in dictionary:
            f.write(elem + "," + dictionary[elem][0] + "," + dictionary[elem][1] + "," + dictionary[elem][2] + "," +
                    dictionary[elem][3] + "," + dictionary[elem][4] + "\n")#запись новых данных в словарь
    f.close()

def add(dictionary):
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            dictionary[line[0]] = line[1:]
            print(line)

def sort(dictionary,sorteddictionary):
    print("Сортировка по дате начала поездки")
    sort = sorted(dictionary.values(),
                  key=lambda x: str(x[0]))#сортировка по дате начала поездки 1(0+1) критерий по строковому критерию
    for i in sort:
        for k in dictionary.keys():
            if dictionary[k] == i:
                sorteddictionary[k] = dictionary[k]#вывод отсортированного списка
                break
    for elem in sorteddictionary:
        print(elem + ".", *sorteddictionary[elem])#вывод айди и остальных элементов словаря

def sort1(dictionary,sorteddictionary1):
    print("Сортировка по сумме")
    sort1 = sorted(dictionary.values(),
                   key=lambda x: int(x[4]))  # сортировка по сумме 5(4+1) критерий по числовому критерию
    for i in sort1:
        for k in dictionary.keys():
            if dictionary[k] == i:
                sorteddictionary1[k] = dictionary[k]#вывод отсортированного списка
                break
    for elem in sorteddictionary1:
        print(elem + ".", *sorteddictionary1[elem])#вывод айди и остальных элементов словаря

def criterium(dictionary):
    print("Вывод информации по критерию")
    for elem in dictionary:
        if int(dictionary[elem][3]) >= 6 and elem != 'id':
            print(elem, *dictionary[elem])

def main():
    dictionary = {}
    sorteddictionary = {}
    sorteddictionary1 = {}
    count()
    add(dictionary)
    sort(dictionary,sorteddictionary)
    sort1(dictionary,sorteddictionary1)
    criterium(dictionary)
    check = input('Введите q для добавления новых данных в список: ')
    if check == "q":
        write_csv()
    for elem in dictionary:
        print(elem, dictionary[elem])
    f.close()


if __name__ == "__main__":
    main()
