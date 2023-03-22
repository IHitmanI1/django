from django.shortcuts import render
from .forms import ProductForm
def new_product(request):
    msg ='Заполните все поля данных'
    if request.method == "POST":
       form = ProductForm(request.POST)
       if form.is_valid():
           product = form.save(commit=False)
           product.save()
           msg = 'Сохранил отлично!'
           return render(request, 'new_product.html', {'form': form, 'message': msg,})
    else:
        form = ProductForm()
    return render(request, 'new_product.html', {'form': form, 'message': msg,})

def index(request):
    return render(request, "index.html")

def simple(request):
    return render(
        request,
        'simple.html',
        {
            'title': 'МЕЧТЫ СБЫВАЮТСЯ',
            'message': '',
        }
    )

def map(request):
    return render(request, 'map.html')

from .models import Product
def product(request):
    products = Product.objects.all()
    return render(request,'product.html',  {'products': products})

from .forms import MyForm
def myform(request):
    msg = ''
    if request.method == "POST":
       form = MyForm(request.POST)
       if form.is_valid():
           name = form.cleaned_data['name']  # чтение поля формы
           age = str(form.cleaned_data['age'])  # чтение поля формы
           print(name)  # для отладки
           print("OK!!!")
           # запись полученных от клиента данных в файл на сервере
           f = open('C:/Users/HITMAN/Desktop/from_client.txt', 'w')
           f.write(name + '\n')
           f.write(age + '\n')
           f.close()
           if name != 'None':
               msg = 'Your Information send to SERVER. OK!!!'
               return render(request, 'my_form.html', {'form': form, 'message': msg})
    else:
        form = MyForm()
    return render(request, "my_form.html", {"form": form})

def game(request):
    return render(request, "game.html")