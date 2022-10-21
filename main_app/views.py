from django.shortcuts import render, redirect 

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')  

def dressess_index(request):
#   dresses = Dress.objects.filter(user=request.user)  
  return render(request, 'dresses/index.html', { 'dresses': dresses })  


class Dress:  
  def __init__(self, name, style, material, description, color):
    self.name = name
    self.style = style
    self.material = material
    self.description = description
    self.color = color

dresses = [
    Dress('Lola', 'Special occasion', 'Satin', 'Trendy cowl neckline with a slim-fit bodice','Taupe'),
    Dress('Malika', 'Coctail', 'Polyester', 'Simmering sequins to sparkle under the moonlit night. V-neckline','Rose gold'),
    Dress('Gabriela', 'Formal', 'Velvet', 'Romantic sweetheart neckline', 'Burgundy'),
]