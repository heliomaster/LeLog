from django.http import HttpResponse
from django.shortcuts import render
#from .models import Logfields
from .forms import LogfieldsForm


def index(request):
    titre = "title"
    # log_fields = Logfields.objects.all()
    # template = loader.get_template("LogBook/index.html")
    context = {"template_title": titre, }
    return render(request,"LogBook/index.html",context)
    #add form
    form = LogfieldsForm()
    context = {
        "title":title,
        "form": form
    }
    return render(request, "index.html", context)




def detail(request,sumup_id):
    return HttpResponse("<h1>2eme page.</h1>")