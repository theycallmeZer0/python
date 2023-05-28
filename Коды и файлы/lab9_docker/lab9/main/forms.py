from django.db import models
from django import forms
from .models import *

#Виды автомобилей
class CarTypeForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return CarTypeForm(request)

    @staticmethod
    def clone_instance(ins):
        return CarTypeForm(instance=ins)

    class Meta:
        model = CarType
        fields = ['model', 'color', 'price']
        widgets = {
                "model": forms.TextInput(attrs={'class': 'input_field'}),
                "color": forms.TextInput(attrs={'class': 'input_field'}),
                "price": forms.NumberInput(attrs={'class': 'input_field'})
        }



#Автомобили
class CarForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return CarForm(request)

    @staticmethod
    def clone_instance(ins):
        return CarForm(instance=ins)

    class Meta:
        model = Car
        fields = ['model_id', 'buy_location', 'owner_FIO']
        widgets = {
                "model_id": forms.Select(attrs={'class': 'input_field'}),
                "buy_location": forms.TextInput(attrs={'class': 'input_field'}),
                "owner_FIO": forms.TextInput(attrs={'class': 'input_field'})
        }



#Проездная точка
class TravelPointForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return TravelPointForm(request)

    @staticmethod
    def clone_instance(ins):
        return TravelPointForm(instance=ins)

    class Meta:
        model = TravelPoint
        fields = ['name', 'main_owner_id']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'input_field'}),
            "main_owner_id": forms.SelectMultiple(attrs={'class': 'input_field'}),
        }



#Владелец проездных точек
class OwnerTravelPointForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return OwnerTravelPointForm(request)

    @staticmethod
    def clone_instance(ins):
        return OwnerTravelPointForm(instance=ins)

    class Meta:
        model = OwnerTravelPoint
        fields = ['FIO', 'age']
        widgets = {
            "FIO": forms.TextInput(attrs={'class': 'input_field'}),
            "age": forms.NumberInput(attrs={'class': 'input_field'}),
        }


#История проездов автомобилей
class CarPassForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return CarPassForm(request)

    @staticmethod
    def clone_instance(ins):
        return CarPassForm(instance=ins)

    class Meta:
        model = CarPass
        fields = ['date_time', 'plate_number', 'car_id', 'travel_point_id']
        widgets = {
            "date_time": forms.DateTimeInput(attrs={'class': 'input_field'}),
            "plate_number": forms.TextInput(attrs={'class': 'input_field'}),
            "car_id": forms.Select(attrs={'class': 'input_field'}),
            "travel_point_id": forms.Select(attrs={'class': 'input_field'}),
        }


#Характеристики проезжающих автомобилей
class DataOfPassingCarForm(forms.ModelForm):

    @staticmethod
    def clone(request):
        return DataOfPassingCarForm(request)

    @staticmethod
    def clone_instance(ins):
        return DataOfPassingCarForm(instance=ins)

    class Meta:
        model = DataOfPassingCar
        fields = ['numberHistory', 'speed', 'driverFIO']
        widgets = {
            "numberHistory": forms.Select(attrs={'class': 'input_field'}),
            "speed": forms.NumberInput(attrs={'class': 'input_field'}),
            "driverFIO": forms.TextInput(attrs={'class': 'input_field'})
        }