from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	streetAddress = models.CharField(max_length=20, null=True)
	city = models.CharField(max_length=20, null=True)
	state = models.CharField(max_length=20, null=True)
	zipCode = models.CharField(max_length=20, null=True)

	def __str__(self):
		return '{0} {1}'.format(self.user.username)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Order(models.Model):
	user = models.ForeignKey('auth.User', related_name ="orders")
	orderDate = models.DateTimeField(default=timezone.now)
	dueDate = models.DateField(auto_now=False)
	answerOne = models.TextField(default='Answer to question one')
	answerTwo = models.TextField(default='Answer to question two')
	answerThree = models.TextField(default='Answer to question three')
	answerFour = models.TextField(default='Answer to question four')
	answerFive = models.TextField(default='Answer to question five')

	def __str__(self):
		return '{}: {}'.format(self.orderDate, self.user.username)



class Image(models.Model):
	order = models.ForeignKey(Order, related_name = "images")
	orderImage = models.ImageField(upload_to='images')


class Note(models.Model):
	user = models.ForeignKey(User, related_name = "notes")
	order = models.ForeignKey(Order, related_name = "notes")
	noteContent = models.TextField(default='note')



