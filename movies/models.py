from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()  # Поле для року, як ціле число

    def __str__(self):
        return f"{self.name} ({self.year})"
