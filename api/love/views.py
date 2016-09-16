from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from love.models import Order, User, Image, Note
from love.serializers import OrderSerializer, UserSerializer, ImageSerializer, NoteSerializer

class OrderList(viewsets.ModelViewSet):
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class ImageList(viewsets.ModelViewSet):
	queryset = Image.objects.all()
	serializer_class = ImageSerializer

class NoteList(viewsets.ModelViewSet):
	queryset = Note.objects.all()
	serializer_class = NoteSerializer

@csrf_exempt
def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    # If authentication was successful, log the user in
    success = True
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)
    else:
        success = False

    data = json.dumps({"success":success})
    return HttpResponse(data, content_type='application/json')
