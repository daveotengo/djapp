from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(request,*args,**kwargs):
    my_context = {
        "my_text" : "This is my text",
        "my_number" : "123213123",
        "my_list" : [12,121,1213]
    }
    return render(request,'home.html',my_context)
    #return HttpResponse("<h1>Hello World</h1>")

def contact_view(request,*args,**kwargs):
    #return HttpResponse("<h1>Contact</h1>")
    return render(request,'contact.html',{'name':request.user})


def about_view(request,*args,**kwargs):
    #return HttpResponse("<h1>About</h1>")
    return render(request,'about.html',{'name':request.user})

def social_view(request,*args,**kwargs):
    return HttpResponse("<h1>Social</h1>")

