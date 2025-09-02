from django.shortcuts import render

def home(request):
    list1=[]
    for i in range(1,1001,1):
        list1.append(fact(i))
    return render(request,"app3/index.html",{"param1":list1})

def fact(num1):
    result=num1
    for i in range(num1-1,0,-1):
        result=result*i
    return result 
