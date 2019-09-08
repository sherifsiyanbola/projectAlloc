from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    regno = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    projecttitle = models.CharField(max_length=250, null=True)
    department = models.CharField(max_length=100, choices=(
        ('csc', 'Computer Science'),
        ('it', 'Information Tecnology'),
        ('se', 'Software Engineering'),
        ('csec', 'Cyber Security')
    ))
    projecttype = models.CharField(max_length=100, choices=(
        ('re', 'Research Work'),
        ('di', 'Design and Implementation')
    ))
    statement = models.TextField()
    aims = models.TextField()
    suplist = models.CharField(max_length=100, choices=(
        ('prof', 'Prof Ahmad Baita Garko'),
        ('dean', 'Dr Abubakar Miyim'),
        ('hodcsc', 'Dr zaharadden'),
        ('kareem', 'Dr Abdulkareem'),
        ('lawan', 'Dr Abba Lawan'),
        ('kzr', 'Ahmad Sani Kazaure'),
        ('garko', 'Haruna Garko'),
        ('eng', 'Muhammad Abbas'),
        ('aml', 'Aminu Lawal'),
        ('mt', 'Muhammad Tukur Usman'),
        ('salisu', 'Sani Salisu')
    ))
    # image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
    