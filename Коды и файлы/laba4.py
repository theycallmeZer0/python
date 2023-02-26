import csv


class Parentlist():
    def __init__(self, key_inp, date1_inp, date2_inp, phone_inp, distance_inp, price_inp):
        self.key_inp = key_inp
        self.date1_inp = date1_inp
        self.date2_inp = date2_inp
        self.phone_inp = phone_inp
        self.distance_inp = distance_inp
        self.price_inp = price_inp

    def __str__(self):
        return f"{self.key_inp}, {self.date1_inp}, {self.date2_inp}, {self.phone_inp}, {self.distance_inp}, " \
               f"{self.price_inp}"

    def __repr__(self):
        return f"{self.key_inp}, {self.date1_inp}, {self.date2_inp}, {self.phone_inp}, {self.distance_inp}, " \
               f"{self.price_inp}"


class l1st(Parentlist):
    def __init__(self, path):
        self.lengh = None
        self.path = path
        self.dictionary = self.fileopen(self.path)

    def __iter__(self):
        return iter(self.dictionary)

    def __next__(self):
        if self.lengh <= len(self.dictionary):
            x = self.lengh
            self.lengh += 1
            return x
        else:
            raise StopIteration

    def __str__(self): #перегрузка __str__ и __repr__
        return '' + '\n'.join([repr(line) for line in self.dictionary])

    def __repr__(self):
        return '' + '\n'.join([repr(line) for line in self.dictionary])

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        if 0 <= item < len(self.dictionary):
            return self.dictionary[item]
        else:
            raise IndexError("Wrong index.")

    def generator(self): # генератор коллекции
        self.lengh = 0
        while self.lengh < len(self.dictionary):
            yield self.dictionary[self.lengh]
            self.lengh += 1

    @staticmethod
    def fileopen(path: str) -> list:  #чтение из файла
        mas = []

        with open(path, "r") as f:
            for line in f:
                (key_inp, date1_inp, date2_inp, phone_inp, distance_inp, price_inp) = line.replace("\n", "").split(",")
                mas.append(Parentlist(key_inp, date1_inp, date2_inp, phone_inp, distance_inp, price_inp))
        return mas
    def add(self, key_inp, date1_inp, date2_inp, phone_inp, distance_inp, price_inp): # добаление записи о новом студенте
        self.dictionary.append(Parentlist(key_inp, date1_inp, date2_inp, phone_inp, distance_inp, price_inp))
        newline = [key_inp, date1_inp, date2_inp, phone_inp, distance_inp, price_inp]
        with open('data.csv', 'a+', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(newline)
        return self.dictionary

    def sortdate(self) -> list: # сортировка по дате начала
        return sorted(self.dictionary, key=lambda x: x.date1_inp)

    def sortphone(self) -> list :# сортировка по номеру телефона
        return sorted(self.dictionary, key=lambda x: x.phone_inp)

    def sortcriterium(self) -> list: # сортировка по критерию
        return [x for x in self.dictionary if x.distance_inp == "18"]


dictionary = l1st('data.csv')
print("Default mas")
for x in dictionary:
    print(x)
print('')

print("Iterator")
iterator = iter(dictionary)
print(next(iterator))
print(next(iterator))

print("\n__str__ ", dictionary, sep='\n')

print("\n__repr__ ", repr(dictionary), sep='\n')

print("\nSorting by date of begin")
for x in dictionary.sortdate():
        print(x)

print("\nSorting by phone")
for x in dictionary.sortphone():
        print(x)

print("\nSorting by criterium")
for x in dictionary.sortcriterium():
        print(x)

print(dictionary.__getitem__(int(input("Enter line pos: "))))

dictionary.add(input('Enter ID: '), input('Enter date and time of begin: '), input('Enter date and time of end: '),
               input('Enter phone number: '), input('Enter distance: '), input('Enter price: '))

