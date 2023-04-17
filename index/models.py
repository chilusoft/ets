from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_image', null=True, blank=True)

    def __str__(self):
        return self.username
    

class Expense(models.Model):
    EXPENSE_TYPE_CHOICES = (
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Entertainment', 'Entertainment'),
        ('Internet', 'Internet'),
        ('Other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    description = models.TextField(null=True, blank=True)
    expense_type = models.CharField(max_length=100, choices=EXPENSE_TYPE_CHOICES)
    expense_date = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)
    expense_proof = models.ImageField(upload_to='expense_proof', default='expense_proof/default.pdf' ,null=True, blank=True)

    def __str__(self):
        return f'{self.description} - {self.amount} - {self.expense_type}'
    
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    expected_return = models.FloatField(default=0.0)
    actial_return = models.FloatField(default=0.0)
    profit = models.FloatField(default=0.0)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    data_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.description} - {self.amount}'
    

