from django.contrib import admin
from django.urls import path,include
from .views import doctorView

urlpatterns = [
    path("adddoctor",doctorView.as_view(),name='adddoctor'),
]
