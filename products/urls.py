from django.urls import path, include
from . import views

urlpatterns = [
    path("<str:brand>/", views.list_product, name="listview"),
    path("<int:pk>", views.detail_product, name="detailview"),

]
