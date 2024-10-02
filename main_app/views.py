from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import FeedingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog, 
    'feeding_form': feeding_form
  })

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  # success_url = '/dogs/{id}'
  
class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']
  
class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'  
  
def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('dog-detail', dog_id=dog_id)
  