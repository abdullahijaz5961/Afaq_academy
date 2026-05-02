from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def admissions(request):
    return render(request, 'admissions.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        messages.success(request, f'Thank you {name}! Your message has been received. We will contact you shortly.')
        return redirect('contact')
    return render(request, 'contact.html')
