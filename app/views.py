from django.shortcuts import render
from .models import Item
# Create your views here.


def video(request):
    data = Item.objects.all()
    return render(request,'video.html',{'data':data})