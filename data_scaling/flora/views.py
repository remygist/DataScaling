from django.shortcuts import render
from .models import Plant, Discoverer
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, "flora/index.html")

def n1problem(request):
    plants = Plant.objects.all()
    context = {
        "plants": plants
    }
    return render(request, "flora/n1problem.html", context)

def n1solution(request):
    plants = Plant.objects.select_related('discoverer').all()
    context = {
        "plants": plants
    }
    return render(request, "flora/n1solution.html", context)

def pagination(request):
    plant_list = Plant.objects.select_related('discoverer').all()
    paginator = Paginator(plant_list, 25)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "flora/pagination.html", {'page_obj':page_obj})