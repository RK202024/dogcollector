from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dog, Toy
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
  toy_ids_dog_has = dog.toys.all().values_list('id')
  toys_dog_doesnt_have = Toy.objects.exclude(id__in=toy_ids_dog_has)   
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog, 
    'feeding_form': feeding_form,
    'toys': toys_dog_doesnt_have
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

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'
    #fields = ['name', 'breed', 'description', 'age']
    
class ToyList(ListView):
    model = Toy
    
class ToyDetail(DetailView):
    model = Toy
    
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'
    
def associate_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.add(toy_id)
  return redirect('dog-detail', dog_id=dog_id)

def remove_toy(request, dog_id, toy_id):
  Dog.objects.get(id=dog_id).toys.remove(toy_id)
  return redirect('dog-detail', dog_id=dog_id)

  