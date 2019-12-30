from django.shortcuts import render

# Create your views here.
def ministries(request):
    return render(request, 'ministries/ministries.html')

def missions(request):
    return render(request, 'ministries/missions.html')

def cministry(request):
    return render(request, 'ministries/cministry.html')

def yministry(request):
    return render(request, 'ministries/yministry.html')

def aministry(request):
    return render(request, 'ministries/aministry.html')