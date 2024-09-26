from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def health_check(request):
    return HttpResponse("OK", status=200)

def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')
