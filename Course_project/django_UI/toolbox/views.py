from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, 'toolbox.html')


def open_hadoop(request):
    return redirect("http://34.70.107.108:9870")


def open_spark(request):
    return redirect("http://34.123.173.103/")


def open_jupyter(request):
    return redirect("http://34.145.33.228/tree")


def open_sonarqube(request):
    return redirect("http://34.83.57.41:80/")
