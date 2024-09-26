from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello Dog!</h1>')

def about(request):
  return HttpResponse('<h1>About the Dog Collector</h1>')

# Create your views here.
