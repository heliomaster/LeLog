from django.shortcuts import render
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
