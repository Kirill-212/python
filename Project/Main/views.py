import form as form
from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from Main.models import currency
from bs4 import BeautifulSoup
from django.template import loader

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

from django.contrib.auth.forms import PasswordChangeForm

# parser
url = 'http://www.nbrb.by/statistics/rates/ratesdaily.asp'
Headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
    'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=Headers, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('tbody').find_all_next('tr')
    name = []
    currency = []
    value = []
    for item in items:
        name.append(item.find('span', class_='text').get_text())
        currency.append(item.find('td', class_='curAmount').get_text())
        res = str(item.find('td', class_='curCours').find('div').get_text())
        value.append(float(res.replace(',', '.')))

    return name, currency, value


def parse():
    html = get_html(url)
    if html.status_code == 200:
        return get_content(html.text)

    else:
        return "Error"


def index(request):
    # q = currunci.objects.all()
    # q.delete()
    i, j, k = parse()
    m = 0
    for s in range(1, 26):
        number = currency.objects.get(id=s)
        number.value = ''
        if number.value != k[m]:
            number.value = k[m]
        if number.value_name != j[m]:
            number.value_name = j[m]
        if number.name != k[m]:
            number.name = k[m]
    m += 1
    # for s in range(len(i)):
    #     currency.objects.create(name=i[s], value_name=j[s], value=k[s])
    templat = loader.get_template('C:/ycheba/python/python/Project/templates/main.html')
    i = currency.objects.order_by('-name')
    context = {'currency': i}

    return HttpResponse(templat.render(context, request))


# Формы

app_url = "/Main/"


class RegisterFormView(FormView):
    # будем строить на основе
    # встроенной в django формы регистрации
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь
    # в случае успешной регистрации.
    # В данном случае указана ссылка на
    # страницу входа для зарегистрированных пользователей.
    success_url = app_url + "login/"
    # Шаблон, который будет использоваться
    # при отображении представления.
    template_name = "reg/register.html"

    def form_valid(self, form):
        # Создаём пользователя,
        # если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    # будем строить на основе
    # встроенной в django формы входа
    form_class = AuthenticationForm
    # Аналогично регистрации,
    # только используем шаблон аутентификации.
    template_name = "reg/login.html"
    # В случае успеха перенаправим на главную.
    success_url = app_url

    def form_valid(self, form):
        # Получаем объект пользователя
        # на основе введённых в форму данных.
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя,
        # запросившего данное представление.
        logout(request)
        # После чего перенаправляем пользователя на
        # главную страницу.
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    # будем строить на основе
    # встроенной в django формы смены пароля
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    # после смены пароля нужно снова входить
    success_url = app_url + 'login/'

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)
