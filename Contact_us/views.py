from django.shortcuts import render

# Create your views here.

def Contact_us(request):
    return render(request, 'Contact_us/contact.html', {})