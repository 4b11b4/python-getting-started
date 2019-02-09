from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, User

# create a ViewSet based on this toturial
# https://www.django-rest-framework.org/tutorial/quickstart/
from rest_framework import viewsets
from .serializers import GreetingSerializer, UserSerializer

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

class GreetingViewSet(viewsets.ModelViewSet):
    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
