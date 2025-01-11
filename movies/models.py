from django.db import models

class Movie(models.Model):
    POSITIONS = [
        ("1", "Movie"),
        ("2", "Series"),
      
    ]
    name = models.CharField(max_length=100)
    year = models.IntegerField()  # Поле для року, як ціле число
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    position = models.CharField(max_length=255, choices=POSITIONS, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"
