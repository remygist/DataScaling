from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.cache import cache
from .models import Plant, Discoverer


# Create your views here.
def index(request):
    return render(request, "flora/index.html")

def n1problem(request):
    # Try to get the cached data
    plants = cache.get('all_plants')

    if not plants:
        # If cache is empty, perform the query
        plants = Plant.objects.all()  # Query to fetch the plants

        # Cache the result for 15 minutes (900 seconds)
        cache.set('all_plants', plants, timeout=900)
        
        print("Cache MISS - Data has been cached.")  # For debugging purposes

    else:
        print("Cache HIT - Data retrieved from cache.")  # For debugging purposes

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
    # Get the offset and limit from the query parameters (defaults to 0 and 25 if not provided)
    offset = int(request.GET.get('offset', 0))
    limit = int(request.GET.get('limit', 25))

    # Fetch the next batch of plants with pagination
    plants = Plant.objects.select_related('discoverer')[offset:offset + limit]
    
    # Prepare the response data
    data = {
        'plants': [
            {'name': plant.name, 'discoverer': plant.discoverer.first_name} for plant in plants
        ],
        'has_more': Plant.objects.count() > offset + limit  # Indicates if there are more records
    }

    return JsonResponse(data)