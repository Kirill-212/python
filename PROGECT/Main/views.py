from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from Main.models import currency, Message, annual_statistics,statistics_users

from bs4 import BeautifulSoup
import requests
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

from django.contrib.auth import logout
from django.contrib.auth.forms import PasswordChangeForm

from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
import json

URL = 'http://www.nbrb.by/statistics/rates/ratesdaily.asp'

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.122 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find('tbody').find_all_next('tr')
    name = []
    currency_name_ = []
    value = []
    for item in items:
        name.append(item.find('span', class_='text').get_text())
        currency_name_.append(item.find('td', class_='curAmount').get_text())
        res = str(item.find('td', class_='curCours').find('div').get_text())
        value.append(float(res.replace(',', '.')))

    return name, currency_name_, value


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        return get_content(html.text)

    else:
        return "Error"


# def detail(request):

#
#     return render(
#         request,
#         "main.html",
#         {
#             "error_message": error_message,
#             "latest_messages":
#                 Message.objects.order_by('-pub_date')[:5]
#         }
#     )
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
        if number.name_currency != k[m]:
            number.name_currency = k[m]

    m += 1
    # for s in range(len(i)):
    #     currency.objects.create(name_currency=i[s], value_name=j[s], value=k[s])
    ret_render = loader.get_template('C:/ycheba/python/python/PROGECT/Main/templates/base_main.html')
    i = currency.objects.order_by('-name_currency')
    context = {'currency': i,"latest_messages":Message.objects.order_by('-pub_date')[:9]}

    return HttpResponse(ret_render.render(context, request))


app_url = '/Main/'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = app_url + "login/"
    template_name = "reg/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "reg/login.html"
    success_url = app_url

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
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


def post(request):
    msg = Message()
    msg.author = request.user
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url)


# def detail(request):
#     error_message = None
#     if "error_message" in request.GET:
#         error_message = request.GET["error_message"]
#
#     return render(
#         request,
#         "main.html",
#         {
#             "error_message": error_message,
#             "latest_messages":
#                 Message.objects.order_by('-pub_date')[:5]
#         }
#     )


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})


def get_data(request, *args, **kwargs):
    date = {
        "sales": 100
    }
    return JsonResponse(date)


class ChartDate(APIView):
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    h = []
    i = []
    q = currency.objects.all()
    authentication_classes = []
    permission_classes = []
    values = []
    name = []

    for s in range(2, 20):
        number = annual_statistics.objects.get(id=s)
        if number.year.year == 2019:
            a = number.value.split(',')
        if number.year.year == 2018:
            b = number.value.split(',')
        if number.year.year == 2017:
            c = number.value.split(',')
        if number.year.year == 2016:
            d = number.value.split(',')
        if number.year.year == 2015:
            e = number.value.split(',')
        if number.year.year == 2014:
            f = number.value.split(',')
        if number.year.year == 2013:
            g = number.value.split(',')
        if number.year.year == 2012:
            h = number.value.split(',')
        if number.year.year == 2011:
            i = number.value.split(',')
        if number.name_currency2_id == 5:
            USD1 = {'2019': [float(x) for x in a], '2018': [float(x) for x in b], '2017': [float(x) for x in c],
                    '2016': [float(x) for x in d], '2015': [float(x) for x in e],
                    '2014': [float(x) for x in f], '2013': [float(x) for x in g],
                    '2012': [float(x) for x in h], '2011': [float(x) for x in i]}
        else:
            EUR1 = {'2019': [float(x) for x in a], '2018': [float(x) for x in b], '2017': [float(x) for x in c],
                    '2016': [float(x) for x in d], '2015': [float(x) for x in e],
                    '2014': [float(x) for x in f], '2013': [float(x) for x in g],
                    '2012': [float(x) for x in h], '2011': [float(x) for x in i]}

    USD = USD1
    EUR = EUR1


    for s in range(1, 26):
        number = currency.objects.get(id=s)
        values.append(number.value)
        name.append(number.name_currency)

    def get(self, request, ):
        value = ChartDate.values
        name_country = ChartDate.name
        date = {
            "value": value,
            "name_country": name_country,
            "EUR": ChartDate.EUR,
            "USD": ChartDate.USD
        }
        return Response(date)



