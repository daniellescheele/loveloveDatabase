from rest_framework import routers
from django.conf.urls import url, include
from love import views

router = routers.DefaultRouter()
router.register(r'orders', views.OrderList)
router.register(r'users', views.UserList)


#add this below
urlpatterns = [
	url(r'^', include(router.urls)),
]
