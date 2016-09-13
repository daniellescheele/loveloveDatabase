from love.models import Order, User
from rest_framework import serializers

class OrderSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
				model = Order
				fields = ('id', 'url', 'dueDate')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      	model = User
      	fields = ('id', 'url', 'firstName', 'lastName')
