import datetime

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


# Create your models here.

def get_role(user):
    template = ""
    if user.is_authenticated:
        if user.is_superuser:
            template = "travel_point_owner"
        elif user.groups.filter(name='travel_point_owner').exists():
            template = "travel_point_owner"
        elif user.groups.filter(name='driver').exists():
            template = "driver"
    return template

#Виды автомобилей
class CarType(models.Model):
    model = models.CharField('Модель', max_length=50, default="")
    color = models.CharField('Цвет', max_length=50, default="")
    price = models.IntegerField(default=0)
    offsetName = 0

    names = ["Индекс", "Модель", "Цвет", "Цена"]
    title = "Виды автомобилей"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": DataOfPassingCar}

    def get_dict(self):
        return {"id": self.id, 0: self.model, 1: self.color, 2: self.price}

    @staticmethod
    def clone():
        return CarType()

    def __str__(self):
        return str(self.id)


#Автомобили
class Car(models.Model):
    model_id = models.ForeignKey('CarType', on_delete=models.CASCADE, default=0)
    buy_location = models.CharField("Локация покупки", max_length=150, default="")
    owner_FIO = models.CharField("ФИО владельца", max_length=150, default="")
    offsetName = 0

    names = ["Индекс", "Индекс модели", "Локация покупки", "Фио владельца"]
    title = "Автомобили"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": DataOfPassingCar}

    def get_dict(self):
        return {"id": self.id, 0: self.model_id, 1: self.buy_location, 2: self.owner_FIO}

    @staticmethod
    def clone():
        return Car()

    def __str__(self):
        return str(self.model_id)



#Проездная точка
class TravelPoint(models.Model):
    name = models.CharField("Название", max_length=150, default="")
    main_owner_id = models.ManyToManyField('OwnerTravelPoint')
    offsetName = 0

    names = ["Индекс", "Название", "Индекс главного владельца"]
    title = "Проездная точка"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": DataOfPassingCar}

    def get_dict(self):
        return {"id": self.id, 0: self.name, 1: ", ".join(map(str, self.main_owner_id.all()))}

    @staticmethod
    def clone():
        return TravelPoint()

    def __str__(self):
        return str(self.id)


#Владелец проездных точек
class OwnerTravelPoint(models.Model):
    FIO = models.CharField("ФИО", max_length=250, default="")
    age = models.IntegerField(default=0)
    offsetName = 0

    names = ["Индекс", "Фио", "Возраст"]
    title = "Владелец проездной точки"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": DataOfPassingCar}

    def get_dict(self):
        return {"id": self.id, 0: self.FIO, 1: self.age}

    @staticmethod
    def clone():
        return OwnerTravelPoint()


    def __str__(self):
        return str(self.id)


#История проездов автомобилей
class CarPass(models.Model):
    date_time = models.DateTimeField(default=datetime.datetime(1, 1, 1, 1, 1))
    plate_number = models.CharField("Номерной знак", max_length=150, default="")
    car_id = models.ForeignKey('Car', on_delete=models.DO_NOTHING, default=0)
    travel_point_id = models.ForeignKey(TravelPoint, on_delete=models.DO_NOTHING, default=0)
    offsetName = 0

    names = ["Номер", "Дата и время", "Номерной знак", "Индекс автомобиля", "Индекс проездной точки"]
    title = "История проезда автомобилей"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": True, "have_field": False, "field_id": 1, "linked_class": DataOfPassingCar}

    def get_dict(self):
        return {"id": self.id, 0: self.date_time, 1: self.plate_number, 2: self.car_id, 3: self.travel_point_id}

    @staticmethod
    def clone():
        return CarPass()

    def __str__(self):
        return str(self.id)


#Характеристики проезжающих автомобилей
class DataOfPassingCar(models.Model):
    numberHistory = models.OneToOneField('CarPass', on_delete=models.CASCADE, default=0)
    speed = models.FloatField()
    driverFIO = models.CharField("Фио водителя", max_length=250, default="")
    offsetName = -1



    names = ["Индекс", "Номер истории", "Скорость", "Фио владельца"]
    title = "Характеристика проезжающих автомобилей"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": True, "have_field": True, "field_id": 1, "linked_class": CarPass}

    def get_dict(self):
        return {"id": self.id,  0: self.numberHistory, 1: self.speed, 2: self.driverFIO}

    @staticmethod
    def clone():
        return DataOfPassingCar()

    def __str__(self):
        return str(self.numberHistory)

class Article(models.Model):
    title = models.CharField('Название', max_length=50, default="")
    anons = models.CharField('Анонс', max_length=250, default="")
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    offsetName = 0

    def __str__(self):
        return self.title
