from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .AuthorizationForms import *

left_lock_tables = 3
right_lock_tables = 5

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

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'role': get_role(request.user)})

def about(request):
    return HttpResponse("<h1>О себе</h1>")


def table_view(request, tk):

    role = get_role(request.user)

    if left_lock_tables <= tk <= right_lock_tables and not role == "travel_point_owner":
        return redirect('main')

    table = []
    model = [CarType, Car, TravelPoint, OwnerTravelPoint, CarPass, DataOfPassingCar]
    title = model[tk].title

    for x in model[tk].objects.all():
        table.append(x.get_dict())

    return render(request, 'main/table_show.html', {'table': table, 'names': model[tk].names, 'title': title, 'table_id': tk, 'role': role})


def table_change(request, tk, el, command):

    role = get_role(request.user)

    if not request.user.is_authenticated:
        return redirect('main')

    if left_lock_tables <= tk <= right_lock_tables and not role == "travel_point_owner":
        return redirect('main')

    forms = [CarTypeForm, CarForm, TravelPointForm, OwnerTravelPointForm, CarPassForm, DataOfPassingCarForm]
    model = [CarType, Car, TravelPoint, OwnerTravelPoint, CarPass, DataOfPassingCar]
    form = forms[tk]
    names = model[tk].names.copy()
    names.pop(0)
    error = ''
    el -= 1

    if command == 'edit':
        form = forms[tk].clone_instance(model[tk].objects.all()[el])

        if request.method == 'POST':
            form = forms[tk].clone(request.POST)
            if form.is_valid():
                edit_model = model[tk].objects.all()[el]
                for name in form.Meta.fields:
                    setattr(edit_model, name, form.cleaned_data.get(name))
                edit_model.save()
                return redirect('table_show', tk)
            else:
                error = 'Данные введены некорректно.'


    if command == 'add':
        if request.method == 'POST':
            form = forms[tk].clone(request.POST)
            if form.is_valid():
                form.save()
                return redirect('table_show', tk)
            else:
                error = 'Данные введены некорректно.'

    if command == 'delete':
        model[tk].objects.all()[el].delete()
        return redirect('table_show', tk)

    return render(request, 'main/form.html', {'form': form, 'names': names, 'error': error, 'role': role})

def login_method(request):

    if not request.user.is_authenticated:
        return redirect('main')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')

    return render(request, 'registration/login.html', {'names': ['Логин', 'Пароль', 'Подтверждение пароля']})

def registration(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Аккаунт зарегестрирован")
            Group.objects.get(name="driver").user_set.add(User.objects.last())
            return redirect('login')
    return render(request, 'registration/registration.html', {'form': form, 'names': ['Логин', 'Пароль', 'Подтверждение пароля'], 'error': messages})