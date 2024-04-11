from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    member = Member.objects.all()
    context ={
        'member':member
    }
    return render(request,'index.html',context)

def add(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')
        mem = Member(first_name=first_name,last_name=last_name,country=country)
        mem.save()
        return redirect('index')
    return render(request,'add.html')

def delete(request,id):
    dele = Member.objects.get(id=id)
    dele.delete()
    return redirect('index')

def update(request,id):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')

        client = Member.objects.get(id=id)

        client.first_name=first_name
        client.last_name=last_name
        client.country=country
        client.save()
        return redirect('index')
    else:
        client = Member.objects.get(id=id)
        context ={
            'client':client
        }

        return render(request,'update.html',context)