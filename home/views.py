from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A view that displays the index page
    """
    render(request, "index.html")