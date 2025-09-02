from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app4/index.html',{'param1':"How are you"})
