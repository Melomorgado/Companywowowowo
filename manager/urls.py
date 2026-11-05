from django.urls import path
from .views import ManagerView

urlpatterns = [
    path('manager/' , view = ManagerView.as_view()),
]