from django.db import models

# Create your models here.

class Retriver(models.Model):
    name = models.CharField(max_length=100);
    email = models.EmailField();
    currentDate = models.DateField();
    gitUrl = models.URLField();

    def __str__(self):
        return self.name, self.email, self.currentDate, self.gitUrl



