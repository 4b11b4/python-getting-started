from rest_framework import routers
from django.urls import include, path
from .views import GreetingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'greetings', views.GreetingViewSet()
router.register(r'users', views.UserViewSet()

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# Because we're using viewsets instead of views, we can automatically generate
# the URL conf for our API, by simply registering the viewsets with a router class.

# Again, if we need more control over the API URLs we can simply drop down to
# using regular class-based views, and writing the URL conf explicitly.
