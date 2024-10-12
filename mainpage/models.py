from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отправки")

    def __str__(self):
        return f"Сообщение от {self.name} ({self.email})"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

