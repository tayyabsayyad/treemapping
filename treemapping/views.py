from django.shortcuts import render, redirect


# Create your views here.
def maptree(request):
    return render(request, 'Home.html', {})
