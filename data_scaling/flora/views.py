from django.shortcuts import render
from .models import Plant, Discoverer

# Create your views here.
def index(request):
    return render(request, "flora/index.html")

def n1problem(request):
    plants = Plant.objects.all()
    context = {
        "plants": plants
    }
    return render(request, "flora/n1problem.html", context)