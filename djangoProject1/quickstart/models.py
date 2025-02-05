from django.db import models

# Create your models here.

class UserData(models.Model):
    name = models.CharField(max_length=100);
    email = models.EmailField();
    currentDate = models.DateField(auto_now=True);
    updated_at = models.DateTimeField(auto_now=True)
    gitUrl = models.URLField();

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'User Data'



