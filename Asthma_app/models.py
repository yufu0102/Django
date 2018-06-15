from django.db import models

# Create your models here.

class Information(models.Model):
	age = models.IntegerField()
	gender = models.CharField(max_length=1)
	smoking = models.CharField(max_length=1)
	BH = models.DecimalField(max_digits=5, decimal_places=2)
	BW = models.DecimalField(max_digits=5, decimal_places=2)
	allergy = models.CharField(max_length=1)
	IgE = models.DecimalField(max_digits=7, decimal_places=2)
	rhinosinusitis = models.CharField(max_length=1)
	PFT = models.IntegerField()
	FVC = models.DecimalField(max_digits=5, decimal_places=2)
	FEV1 = models.DecimalField(max_digits=5, decimal_places=2)
	PAH = models.DecimalField(max_digits=10, decimal_places=9)