from django.shortcuts import render

def service_info(request):
    return render(request, 'info/service_info.html')