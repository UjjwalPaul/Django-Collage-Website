from django.urls import path
from. import views

urlpatterns = [
    path('',views.home),
    path('login', views.login),
    path('registration', views.registration),
    path('signup', views.signup),
    path('logintask',views.logintask),
]
