from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import AccessoryForm
from .models import Accessory, Dress, Wishlist
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view


class DressCreate(LoginRequiredMixin, CreateView):
    model = Dress
    # fields = '__all__'
    fields = ('name', 'style', 'material',
              'description', 'color', 'img_url', 'price')
    # success_url = '/dresses/'

    def form_valid(self, form):
        # assign the logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)


class DressUpdate(LoginRequiredMixin, UpdateView):
    model = Dress
    fields = ('name', 'style', 'material',
              'description', 'color', 'img_url', 'price')
    # success_url = '/dresses/'


class DressDelete(LoginRequiredMixin, DeleteView):
    model = Dress
    success_url = '/dresses/'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def dressess_index(request):
    context = {}
    context["dresses"] = Dress.objects.all()
    return render(request, 'dresses/index.html', context)
    # return render(request,'dresses/index.html', {'dresses': dresses})


@login_required
def dress_index(request):
    dresses = Dress.objects.filter(user=request.user)
    return render(request, 'dresses/index.html', {'dresses': dresses})
    
   

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

@login_required
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
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# @login_required
# def add_review(request, dress_id):
#   dress = Dress.objects.get(id = dress_id)
#   if request.method == 'POST':
#     form = ReviewForm(request.POST)
#     if form.is_valid():
#       review= form.save(commit=False)
#       review.dress= dress
#       review.user=request.user
#       review.save()
#       return redirect('detail',dress_id)
#   else:
#     form= ReviewForm()
#   return render(request, 'reviews/add.html', {"form": form })

def wishlist(request):
    return render(request, 'new.html')