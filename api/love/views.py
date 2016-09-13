from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from love.models import Order, User
from love.serializers import OrderSerializer, UserSerializer

class OrderList(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

class UserList(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
