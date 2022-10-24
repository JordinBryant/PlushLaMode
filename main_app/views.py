from django.shortcuts import render, redirect
from .forms import AccessoryForm
from .models import Accessory, Dress
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

@login_required
def dressess_index(request):
    context = {}
    context["dresses"] = Dress.objects.all()
#   dresses = Dress.objects.filter(user=request.user)
    return render(request, 'dresses/index.html', context)


@login_required
def dress_index(request):
    dresses = Dress.objects.filter(user=request.user)
    return render(request, 'dresses/index.html', {'dresses': dresses})


# def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

@login_required
def dresses_detail(request, dress_id):
    dress = Dress.objects.get(id=dress_id)
    accessories = Accessory.objects.filter(dress=dress_id)
    return render(request, 'dresses/detail.html', {'dress': dress, 'accessories': accessories})

@login_required
def list_accessories(request, dress_id):
    accessories = Accessory.objects.all()
    return render(request, 'accessories/new.html', {'accessories': accessories, 'dress_id': dress_id})

@login_required
def add_accessory(request, dress_id, accessory_id):
    accessory = Accessory.objects.get(id=accessory_id)
    dress = Dress.objects.get(id=dress_id)
    accessory.dress = dress
    accessory.save()
    return redirect('detail', dress_id)


def all_accessories(request):
    accessories = Accessory.objects.all()
    return render(request, 'accessories/all.html', {'accessories': accessories})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)          
