from django.shortcuts import render
from .models import Logfields


def index(request):
    posts = Logfields.object.pic_field()
    return render(request, "index.html", {'posts': posts})
