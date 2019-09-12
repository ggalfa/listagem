from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField(blank=True, null=True)
    date_event = models.DateTimeField(verbose_name='Data do Evento')
    date_create = models.DateTimeField(auto_now=True, verbose_name='Criado')
    usuer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
