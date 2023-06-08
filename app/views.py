from django.shortcuts import render

# Create your views here.
def boot(request):
    return render(request, 'htmlfile.html')
def boot_down(request):
    return render(request, 'boot_down.html')