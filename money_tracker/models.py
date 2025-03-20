from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)

    def __str__(self):
        return self.username


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('cloth', 'Clothing'),
        ('transport', 'Transport'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=55,decimal_places=2)
    expense_name = models.CharField(null=True,blank=True)
    date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.category} - {self.amount} - {self.date}'


