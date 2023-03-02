from django.db import models


class Menu(models.Model):
    name = models.CharField("Название меню", max_length=100, unique=True)
    parent = models.ForeignKey(
        "self", models.CASCADE, verbose_name="родитель", blank=True, null=True
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self) -> str:
        return self.name
