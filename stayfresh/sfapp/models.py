from django.db import models

# Create your models here.

class Customer(models.Model):
	ID        = models.CharField('ID', max_length=50)
	firstName = models.CharField('First Name', max_length=50)
	lastName  = models.CharField('Last Name', max_length=50)
	notes     = models.CharField('Notes', max_length=500)

	def __str__(self):
		return self.ID

class Transaction(models.Model):
	SIZES = (
		('S', 'Small'),
		('M', 'Medium'),
		('L', 'Large'),
		('XL', 'Extra Large')
	)
	SALE_TYPE = (
		('C', 'Cosignment'),
		('B', 'Buyout'),
		('S', 'Sale'),
		)
	customer  = models.ForeignKey(Customer,on_delete=models.CASCADE)
	size      = models.CharField(max_length=1, choices=SIZES)
	sale_type = models.CharField(max_length=1, choices=SALE_TYPE)
	Price     = models.PositiveIntegerField()
