from django.shortcuts import render
from .models import Contact


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'products.html')


def services(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            phone=phone,
            message=message
        )

        return render(request, 'contact.html', {'success': True})

    return render(request, 'contact.html')