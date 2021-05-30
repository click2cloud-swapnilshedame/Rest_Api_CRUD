
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.EmployeeTables.as_view()),
    path('Emp/<int:pk>',views.EmpUpdate.as_view())
]