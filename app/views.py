import sys
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect

from .models import Note
from .forms import noteform
from django.contrib import messages

# Create your views here.
def readall(request):
    print(sys.path)
    notes = Note.objects.all()
    return render(request, 'allnotes.html', {'list': notes})

def create(request):
    if request.method=='POST':
        form=noteform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Post Created')
            return render(request, 'allnotes.html', {'list':Note.objects.all()})
    else:
        form=noteform()
    return render (request,'create.html',{'form':form})

def deletenote(request,pk):
    if request.method=='POST':
        note=Note.objects.get(id=pk)
        note.delete()
    return HttpResponseRedirect('/')


def updatenote(request,id):
    if request.method=='POST':
        note=Note.objects.get(pk=id)
        note.date
        form=noteform(request.POST,instance=note)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Post updated')
            return render(request, 'allnotes.html', {'list':Note.objects.all()})
    else:
        note = Note.objects.get(pk=id)
        form=noteform(instance=note)
    return render (request,'update.html',{'form':form})

