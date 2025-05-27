from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import Person
import random
from datetime import date
from rest_framework.response import Response
# Create your views here.

class View(viewsets.ModelViewSet):
  serializer_class = Serializer
  queryset = Person.objects.all()


class rand_five(viewsets.ModelViewSet):
  serializer_class = rand_five_serializer
  def get_queryset(request):
    random.seed(str(date.today()))

    p1, p2, p3 = random.sample(range(1, 1000), 3)
    p4 = random.randint(1001, 5000)
    p5 = random.randint(5001, 10000)
    print([p1, p2, p3, p4, p5])
    queryset = Person.objects.filter(popularity__in=[p1, p2, p3, p4, p5])

    return queryset
