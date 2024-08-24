from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return HttpResponse('<h1><marquee>msd is the best wicketkeeper and batsman</marquee></h1>')

def raina(request):
    return render(request,'raina.html')