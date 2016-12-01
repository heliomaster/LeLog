from django.http import HttpResponse
from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponseRedirect
from django.template import loader

from .forms import NameForm


# Create your views here.
def get_name(request):
    template = loader.get_template('name.html')
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/THANKS/')

    else:
        form = NameForm()
    return render(request, 'name.html', {'form':form})
=======
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
>>>>>>> airportcode
