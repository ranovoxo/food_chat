from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'foodie_chat/templates/welcome.html', {'today': datetime.today()})