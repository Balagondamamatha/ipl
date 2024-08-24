from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rohit(request):
    return HttpResponse('<h1>rohit is the best batsman</h1>')

def hardik(request):
    return render(request,'hardik.html')