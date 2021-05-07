from django.http import HttpResponseRedirect
from django.shortcuts import render

import logging, time


# Get an instance of a logger
logger = logging.getLogger("django")

from .forms import NameForm


def index(request):
    # if this is a POST request we need to process the form data
    context = ""

    if request.method == 'POST':
        if len(request.POST["input"]) > 0:
            logger.error(request.POST["input"])
        time.sleep(1)
        # create a form instance and populate it with data from the request:
        form = NameForm()
        # check whether it's valid:
        if NameForm(request.POST).is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print("ok")

            with open("ex02/history.log", "r") as f:
                context = f.read().split("\n")
            return render(request, 'form.html', {'form': form, 'context': context})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    with open("ex02/history.log", "r") as f:
        context = f.read().split("\n")
    return render(request, 'form.html', {'form': form, 'context': context})



