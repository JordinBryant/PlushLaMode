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
  def __init__(self,style, name, material, description, color):
    self.style = style
    self.name = name
    self.material = material
    self.description = description
    self.color = color

dresses = [
    Dress('Special Occasion', 'Lola', 'Satin', 'trendy cowl neckline with a slim-fit bodice','Taupe'),
    Dress('Coctail', 'Malika', 'Polyester', 'Simmering sequins to sparkle under the moonlit night. V-neckline','Rose gold'),
    Dress('Formal', 'Gabriela', 'Velvet', 'Romantic sweetheart neckline', 'Burgundy'),
]