from django.shortcuts import render,redirect
from .forms import   TodoModelForm
from .models import Todo

# Create your views here.
def index(request):
    form = TodoModelForm()
    return render(request,"todo/index.html",{"form":form})




def salom(request):
    if request.method == "POST":
        form = TodoModelForm(request.POST)
    if form.is_valid():
       form.save()
    else:
        print("form valid emas ekan ")
        print(form.errors)
        return render(request,"todo/index.html",{   "form":form})
    return redirect("/")
    
def hayr(request):
    return render(request,"todo/hayr.html")
    
        
        