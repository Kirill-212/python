from django.urls import path

from . import views
from .views import index, HomeView, ChartDate

urlpatterns = [
    path('', index),
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('password-change/', views.PasswordChangeView.as_view()),
    path('post/', views.post, name='post'),
    path('charts/', HomeView.as_view(), name='home'),
    path('charts/chart/date', ChartDate.as_view()),



]
