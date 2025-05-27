from rest_framework import serializers
from .models import Person

class Serializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ('name', 'dob', 'dod', 'gender', 'popularity', 'occupation', 'country')

class rand_five_serializer(serializers.ModelSerializer):
  class Meta:
    model = Person
    fields = ('name', 'dob', 'dod', 'gender', 'popularity', 'occupation', 'country')