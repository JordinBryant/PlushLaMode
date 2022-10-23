from django.shortcuts import render, redirect

from .forms import AccessoryForm
from .models import Accessory, Dress

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dressess_index(request):
    context = {}
    context["dresses"] = Dress.objects.all()
#   dresses = Dress.objects.filter(user=request.user)
    return render(request, 'dresses/index.html', context)


# class Dress:
#   def __init__(self, name, style, material, description, color):
#     self.name = name
#     self.style = style
#     self.material = material
#     self.description = description
#     self.color = color


# dresses = [
#     Dress('Lola', 'Special occasion', 'Satin', 'Trendy cowl neckline with a slim-fit bodice','Taupe'),
#     Dress('Malika', 'Coctail party', 'Polyester', 'Simmering sequins to sparkle under the moonlit night. V-neckline','Rose gold'),
#     Dress('Gabriela', 'Formal affair', 'Velvet', 'Romantic sweetheart neckline', 'Burgundy'),
#     Dress('Gia','Night Club', 'Satin', 'Sleeveless square neckline. Ruched body', 'Ivory'),
#     Dress('Ari', 'Casual date', 'Nylon', 'Spaghetti straps, bodycon silhouette','Black'),
# ]

def dress_index(request):
    dresses = Dress.objects.all()
    return render(request, 'dresses/index.html', {'dresses': dresses})


def dresses_detail(request, dress_id):
    dress = Dress.objects.get(id=dress_id)
    accessories = Accessory.objects.filter(dress=dress_id)
    return render(request, 'dresses/detail.html', {'dress': dress, 'accessories': accessories})


def create_accessory(request, dress_id):
    print(Dress.objects.get(id=dress_id))
    if request.method == "POST":
        form = AccessoryForm(request.POST)
        if form.is_valid():
            new_accessory = Accessory(form)
            new_accessory.dress = Dress.objects.get(id=dress_id)
            new_accessory.save()
    else:
        form = AccessoryForm()
    return render(request, 'accessories/new.html', {"form": form})
