from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, World!")
def search_flight(request):
    return render(request, 'flight_search.html')
# Create your views here.
