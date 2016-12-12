from django.shortcuts import render
from .forms import LogfieldsForm


def index(request):
    title ="welcome"
    form = LogfieldsForm(request.POST or None)
    context = {"title": title,
                "form":form}
    # passe les validation de form
    if form.is_valid():
        # creation variable instance si je veux faire d'autre validation par ex
        instance = form.save(commit=False)
        instance.save()
        context = {"title": "THANK YOU"}


    return render(request, "index.html", context)
