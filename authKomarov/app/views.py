from django.shortcuts import render
from .forms import UserAuthenticationForm
from .models import User

def authentication(request):
    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            user = request.POST.get("username")
            pas = request.POST.get("password")
            user = User.objects.filter(username=user, password=pas)
            print(user)
            print(pas)
            if user.exists():
                template = "index.html"
                return render(request, template)
                #  переходим на сайт, а надо сравнить с данными БД
            return render(request, 'authentication.html', {'form': form, 'msg': 'Этого пользователя нет в базе!'})
    else:
        form = UserAuthenticationForm()
    return render(request, 'authentication.html', {'form': form, 'msg': 'Заполните поля и нажмите кнопку!'})

def index(request):
    return render(request, "index.html")

