from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="emp_home"),
    path("list/", views.employee_list, name="employee_list"),
    path("employee/<int:emp_id>/", views.employee_detail, name="employee_detail"),
    path("about/", views.about, name="emp_about"),
    path("contact/", views.contact, name="emp_contact"),
]
