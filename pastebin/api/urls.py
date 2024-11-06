from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('', Main.as_view(), name="home"),
    path('<slug:unique_hash>/', check_text, name='text'),
    path('<str:unique_hash>/update/', UpdateText.as_view(), name='update_page'),

]