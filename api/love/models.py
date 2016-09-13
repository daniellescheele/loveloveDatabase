from django.db import models
from django.utils import timezone

class Order(models.Model):
	orderId =
	userId
	orderDate = models.DateTimeField(auto_now_add=True)
	dueDate = models.DateField(auto_now=False)
	answerOne = models.TextField()
	answerTwo = models.TextField()
	answerThree = models.TextField()
	answerFour = models.TextField()
	answerFive = models.TextField()



class User(models.Model):
	firstName = models.CharField(max_length=20)
	lastName = models.CharField(max_length=20)

	def __str__(self):
		return '{0} {1}'.format(self.firstName, self.lastName)


