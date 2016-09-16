from rest_framework import routers
from django.conf.urls import url, include
from love import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'orders', views.OrderList)
router.register(r'users', views.UserList)
router.register(r'images', views.ImageList)
router.register(r'notes', views.NoteList)


#add this below
urlpatterns = [
	url(r'^login$', views.login_user, name='login'),
	url(r'^', include(router.urls)),
]
