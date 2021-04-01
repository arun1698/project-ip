from django.http import HttpResponse

from django.shortcuts import render


def index(request):
    return HttpResponse("<h1> you are watching homepage</h1>")
def rend_demo(request):
    return render(request,"sample.html")
def sam_demo(request):
    return render(request,"html_demo/sample.html")

