from rest_framework import serializers
from .models import Greeting, User

class GreetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Greeting
	fields = ('when', 'name')

# What is the difference between a Hyperlinked and regular Model serializer?
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
	fields = ('name')
