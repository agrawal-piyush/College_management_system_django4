from django.shortcuts import render
from .models import Student
from .forms import StudentForm

def home(request):
    return render(request,'home.html')

def add(request):
    form = StudentForm()
    context ={'form':form}
    return render(request,'add.html',context)

def update(request):
    return render(request,'update.html')

def delete(request):
    return render(request,'delete.html')

def search(request):
    return render(request,'Search.html')

def addsuccess(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            s = Student(S_id = form.cleaned_data['S_id'],name= form.cleaned_data['name'], Branch= form.cleaned_data['Branch'],Year=form.cleaned_data['Year'])
            s.save()
    return render(request,'addsuccess.html')
