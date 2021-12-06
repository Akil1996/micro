from django.shortcuts import render

# Create your views here.
def festival_home(request):
    return render(request, "home.html", {})