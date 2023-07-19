from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def srujana(request):
    return HttpResponse('Tinnavara')
def srujana(request):
    return render(request,'srujana.html')