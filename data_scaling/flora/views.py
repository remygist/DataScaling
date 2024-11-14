from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.cache import cache
from .models import Plant, Discoverer
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, "flora/index.html")

def n1problem(request):
    plants = cache.get('all_plants')

    if not plants:
        plants = Plant.objects.all()  

        cache.set('all_plants', plants, timeout=900) 
        print("Cache MISS - Data has been cached.")  
    else:
        print("Cache HIT - Data retrieved from cache.")  

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

def infinite_scroll_view(request):
    return render(request, "flora/infinite_scroll.html")

def infinite_scroll_plants(request):
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 25))

    plants = Plant.objects.select_related('discoverer')[offset:offset + limit]
    
    data = {
        'plants': [
            {'name': plant.name, 'discoverer': plant.discoverer.first_name} for plant in plants
        ],
        'has_more': Plant.objects.count() > offset + limit 
    }

    return JsonResponse(data)


def search_plants(request):
    search_term = request.GET.get('q', '')
    limit = 50  # Adjust as needed

    if search_term:
        plants = Plant.objects.filter(
            Q(name__icontains=search_term) | Q(discoverer__first_name__icontains=search_term)
        ).select_related('discoverer')[:limit]
    else:
        plants = Plant.objects.all().select_related('discoverer')[:limit]

    data = {
        "plants": [
            {
                "name": plant.name,
                "discoverer_first_name": plant.discoverer.first_name
            }
            for plant in plants
        ]
    }
    return JsonResponse(data)