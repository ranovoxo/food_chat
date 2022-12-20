from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


def request_page(request):
    if(request.path == '/login/'):
        return render(request, 'home/login.html', {})
    else:
        return None