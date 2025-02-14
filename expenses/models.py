from django.db import models

# Create your models here.
class MyExpenses(models.Model):
    amount = models.IntegerField()
    CATEGORY_CHOICES = [
    ('food', 'Food'),
    ('transport', 'Transport'),
    ('entertainment', 'Entertainment'),
    ('bills', 'Bills'),
    ('other', 'Other'),
]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateTimeField()
    description = models.TextField()
    
    def __str__(self):
        return self.category
    