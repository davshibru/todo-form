from django.db import models
from django.conf import settings

class To(models.Model):
	todo = models.CharField(max_length=50)
	CHOISE = (('doing','doing'),('done','done'),('cancer','cancer'))
	action = models.CharField(
		max_length=20, 
		choices=CHOISE,
		default='doing',
		)


	def __str__(self):
		return self.todo

# Create your models here.
