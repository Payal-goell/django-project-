from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("task1/", views.result_portal, name="result_portal"),
    path("task2/", views.shopping, name="shopping"),
    path("task7/", views.hotel_rooms, name="hotel_rooms"),
    path("task9/", views.loan_checker, name="loan_checker"),
]
