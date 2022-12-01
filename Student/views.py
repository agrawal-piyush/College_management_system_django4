from django.http import HttpResponse
from django.shortcuts import render
from .models import Student
from .forms import StudentForm,LoginForm,UserRegform

from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    d = Student.objects.all().values()
    x ={ 'data':d}
    return render(request,'home.html',x)

@login_required
def add(request):
    form = StudentForm()
    context ={'form':form}
    return render(request,'add.html',context)

def update(request,id):
    st= Student.objects.get(S_id = id)

    return render(request,'update.html',{'data':st})
def updaterecord(request,id):
    stu = Student.objects.get(S_id=id)
    stu.name = request.POST['name']
    stu.Branch = request.POST['Branch']
    stu.Year = request.POST['Year']
    stu.save()

    return render(request,'addsuccess.html')

@login_required
def data(request):
    d = Student.objects.all().values()
    x ={ 'data':d}
    #print(d)
    return render(request,'data.html',x)

def delete(request,id):
    obj= Student.objects.get(S_id=id)
    obj.delete()
    return render(request,'addsuccess.html')

def addsuccess(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            s = Student(name= form.cleaned_data['name'], Branch= form.cleaned_data['Branch'],Year=form.cleaned_data['Year'])
            s.save()
    return render(request,'addsuccess.html')

def user_login(request):
    if request.method=='POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            user =authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated')
                else:
                    return HttpResponse('Disabled')

            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request,'registration/login.html',{'form':form})
def register(request):
    if request.method == 'POST':
        user_form =UserRegform(request.POST)
        if user_form.is_valid():
            new = user_form.save(commit=False)
            new.set_password(user_form.cleaned_data['password'])
            new.save()
            return render(request,'registration/register_done.html',{'user':new})
    else:
        user_form = UserRegform()
    return render(request,'registration/register.html',{'user_form':user_form})