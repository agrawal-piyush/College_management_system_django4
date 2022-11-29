from django.shortcuts import render
from .models import Student
from .forms import StudentForm
def home(request):

    d = Student.objects.all().values()
    x ={ 'data':d}
    return render(request,'home.html',x)

    return render(request,'home.html')

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
