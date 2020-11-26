from django.db import models

class TEST(models.Model):
    pole1 = models.CharField(max_length=200)
    pole2 = models.DateTimeField('date published')
# Create your models here.
