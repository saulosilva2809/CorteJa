from django.db import models

from apps.base.models import BaseModel


class ClientModel(BaseModel):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name
