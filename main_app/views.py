from django.shortcuts import render

class Dog:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Stevie', 'hound', 'Young and restless.', 3),
  Dog('Genghis', 'frenchie', 'Badly behaved but very polite.', 0),
  Dog('Pippa', 'mix', 'Speaks with her tail.', 4),
  Dog('Bowie', 'scottie', 'Always the the older brother.', 6)
]


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })