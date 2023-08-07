from django.shortcuts import render

# Create your views here.

def portfilio(request):
    return render(request, 'Portfilio/portfilio.html', {})