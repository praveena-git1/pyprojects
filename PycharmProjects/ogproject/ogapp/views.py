from django.shortcuts import render,redirect
from .models import employee
# Create your views here.

def add(request):
    if request.method == "POST":
        employee_obj = employee()
        employee_obj.id = request.POST.get('id')
        employee_obj.name= request.POST.get('name')
        employee_obj.place=request.POST.get('place')
        employee_obj.joining_date=request.POST.get('joining_date')
        employee_obj.image12c=request.POST.get('image')
        employee_obj.save()
        return redirect('/add')
    return render(request,'employeeid.html')

def home(request):
    employee_obj=employee.objects.all()
    return  render(request,'home.html',context={'data':employee_obj})

def delete(request,id):
    employee_obj=employee.objects.get(id=id)
    employee_obj.delete()

    return redirect('/home')

def update(request,id):
    employee_obj = employee.objects.get(id=id)
    if request.method == "POST":
        employee_obj.id = request.POST.get('id')
        employee_obj.name = request.POST.get('name')
        employee_obj.place = request.POST.get('place')
        employee_obj.joining_date = request.POST.get('joining_date')
        employee_obj.save()
        return redirect('/home')
    return render(request, 'edit.html', {'data': employee_obj})
