from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def vk(request):
    return HttpResponse('<h1>vk is the best batsman for rcb</h1>')

def abd(request):
    return render(request,'abd.html')