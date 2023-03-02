from django.shortcuts import render
from django.views.generic import DetailView, View

from .models import Menu


class MenuDetailView(DetailView):
    model = Menu
    context_object_name = "menu"


class MainView(View):
    def get(self, request):
        electronics = Menu.objects.get(name="Электроника")
        appliances = Menu.objects.get(name="Бытовая техника")
        return render(
            request,
            "menu_app/main.html",
            {
                "electronics": electronics,
                "appliances": appliances,
            },
        )
