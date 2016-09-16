from love.models import Order, Profile, User, Image, Note
from rest_framework import serializers

class OrderSerializer(serializers.HyperlinkedModelSerializer):
		class Meta:
				model = Order
				fields = ('id', 'url', 'user', 'orderDate', 'dueDate', 'answerOne', 'answerTwo', 'answerThree', 'answerFour', 'answerFive')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      	model = Profile
      	fields = ('id', 'url', 'username', 'streetAddress', 'city', 'state', 'zipCode')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      	model = Image
      	fields = ('id', 'url', 'order', 'orderImage')

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      	model = Note
      	fields = ('id', 'url', 'order', 'noteContent')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      	model = User
      	fields = ('id', 'url', 'username')
