from . import views
from django.conf.urls import url

app_name = 'Main'
urlpatterns = [

    url('', views.index, name='index'),
    url('register/', views.RegisterFormView.as_view()),
    url('login/', views.LoginFormView.as_view()),
    url('logout/', views.LogoutView.as_view()),
    url('password-change/', views.PasswordChangeView.as_view()),
]
