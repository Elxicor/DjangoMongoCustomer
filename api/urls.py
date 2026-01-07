from django.urls import path
from . import views

urlpatterns = [
    path("customers/", views.customers),
    path("mongo-info/", views.mongo_info),
]
