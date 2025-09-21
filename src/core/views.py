from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Django is up!")

# Create your views here.
