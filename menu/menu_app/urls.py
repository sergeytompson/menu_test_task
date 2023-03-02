from django.urls import path

from .views import MainView, MenuDetailView

urlpatterns = [
    path("menu/<int:pk>", MenuDetailView.as_view(), name="menu"),
    path("", MainView.as_view(), name="main"),
]
