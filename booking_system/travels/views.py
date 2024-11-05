from django.shortcuts import render
from .models import Travel

# Create your views here.

def index(request):
    """
    Renders the index page with all travel entries.
    """
    travels = Travel.objects.all()  # Retrieve all travel records
    return render(request, "travels/index.html", {"travels": travels})

def travel(request, travel_id):
    """
    Renders the details page for a specific travel entry.
    """
    travel = Travel.objects.get(pk=travel_id)  # Retrieve the travel record by its primary key (ID)
    return render(request, "travels/travel.html", {"travel": travel})
