from django.urls import path
from .views import ManagerView
urlpatterns = [
    path('manager/', ManagerView.as_view()),

]