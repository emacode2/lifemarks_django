
# Create your views here.
from django.shortcuts import render

from .models import Mark

def mark_list(request):
    marks = Mark.objects.all()
    return render(request, 'lifemarks/mark_list.html', {'marks': marks})
