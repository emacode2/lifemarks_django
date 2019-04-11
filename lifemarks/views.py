
# Create your views here.
from django.shortcuts import render, redirect
from .forms import MarkForm

from .models import Mark

def mark_create(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            mark = form.save()
            return redirect('mark_detail', pk=mark.pk)
    else:
        form = MarkForm()
    return render(request, 'lifemarks/mark_form.html', {'form': form})

def mark_list(request):
    marks = Mark.objects.all()
    return render(request, 'lifemarks/mark_list.html', {'marks': marks})

def mark_detail(request, pk):
    mark = Mark.objects.get(id=pk)
    return render(request, 'lifemarks/mark_detail.html', {'mark': mark}) 

def mark_edit(request, pk):
    mark = Mark.objects.get(pk=pk)
    if request.method == "POST":
        form = MarkForm(request.POST, instance=mark)
        if form.is_valid():
            mark = form.save()
            return redirect('mark_detail', pk=mark.pk)
    else:
        form = MarkForm(instance=mark)
    return render(request, 'lifemarks/mark_form.html', {'form': form}) 

def mark_delete(request, pk):
    Mark.objects.get(id=pk).delete()
    return redirect('mark_list')
