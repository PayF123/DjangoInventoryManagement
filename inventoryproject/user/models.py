from django.db import models
from django.contrib.auth.models import User

# Create your models here.
DEPARTMENTS = (
    ('Sales', 'Sales'),
    ('Finance', 'Finance')
)

class Profile(models.Model):
    staff = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=50,null=True)
    image = models.ImageField(default='avtar.jpg',
                              upload_to='profile_images')
    department = models.CharField(max_length=50, choices=DEPARTMENTS)

    def __str__(self):
        return f'{self.staff.username}-{self.department}'