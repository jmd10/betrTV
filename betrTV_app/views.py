from django.shortcuts import render

# Create your views here.

def index(request):
    ''' The home page for betrTV_app '''

    return render(request, 'betrTV_app/index.html')
    
