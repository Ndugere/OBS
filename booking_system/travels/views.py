from django.shortcuts import render
from .models import Travel

# Create your views here.

def index(request):
    """
    Renders the index page with all travel entries.
    """
    travels = Travel.objects.all()  # Retrieve all travel records
    return render(request, "travels/index.html", {"travels": travels})
