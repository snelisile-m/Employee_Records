from django.shortcuts import render, redirect
from .forms import EmployeeForm  
from .models import Employee  
# Create your views here.  

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form}) 

 
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  


def edit(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return redirect("/show")

    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        try:
            form.save()
            return redirect("/show")
        except Exception as e:
            print(f"An error occurred: {e}")
    return render(request, 'edit.html', {'employee': employee})

def delete(request, id):
    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return redirect("/show")

    employee.delete()
    return redirect("/show")