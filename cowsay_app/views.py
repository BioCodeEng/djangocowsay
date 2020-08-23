from django.shortcuts import render
import subprocess

from cowsay_app.models import CowText
from cowsay_app.forms import CowForm

def index_view(request):
    if request.method == "POST":
        form = CowForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data.get("text")
            CowText.objects.create(text=text)
            cow_process = subprocess.run(
                f"cowsay '{text}'", capture_output=True, shell=True
            ).stdout.decode("utf-8")
            form = CowForm()
            return render(request, "index.html", {
                "form": form,
                "welcome": "What does the cow say?",
                "subprocess": cow_process
            })

    form = CowForm()
    return render(request, "index.html", {"form": form, "welcome": "The cow says"})


def history_view(request):
    cows = CowText.objects.all().order_by('-id')[:10]
    return render(request, "history.html", {"cowsay": cows})

