from django.urls import path
from .views import EmployeeList

urlpatterns = [
    path('', EmployeeList.as_view()),
]