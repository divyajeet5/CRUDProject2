from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg_dis.as_view(), name="regdis"),
    path('update/<int:id>/', views.modify_data.as_view(), name="moddat"),
    path('delete/<int:id>/', views.delete_data.as_view(), name="deldat"),


]