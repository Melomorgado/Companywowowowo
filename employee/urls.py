from django.urls import path
from .views import EmployeeListView

urlpatterns = [
    path('employee/', EmployeeListView.as_view(), name='employee-list'),
]