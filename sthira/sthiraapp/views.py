from django.shortcuts import render,redirect
from . models import Service
from . forms import Serviceform
from django.http import HttpResponse

# Create your views
def service(request):
    services=Service.objects.all()
    context={
        'service_type':services
    }
    return render(request,'service.html',context)

def detail(request,service_id):
    det=Service.objects.get(id=service_id)
    return render(request,'detail.html',{'det':det})

def add_service(request):
    if request.method=="POST":
        type=request.POST.get('type',)
        desc = request.POST.get('desc',)
        img=request.FILES['img']
        service=Service(type=type,desc=desc,img=img)
        service.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    service=Service.objects.get(id=id)
    form=Serviceform(request.POST or None,request.FILES,instance=service)
    if form. is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'service':service})

def delete(request,id):
    if request.method == "POST":
        service = Service.objects.get(id=id)
        service.delete()
        return redirect('/')
    return render(request, 'delete.html')