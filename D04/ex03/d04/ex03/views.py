from django.shortcuts import render


def index(request):
    return render(request, "index.html", {"color_list": list(range(255, 0, -5))})
