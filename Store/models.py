from django.db import models

# Create your models here.

class Diary(models.Model):
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name


