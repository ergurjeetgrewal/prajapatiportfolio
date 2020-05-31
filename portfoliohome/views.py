#custom made
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from portfoliohome.models import Contact
from django.contrib import messages
def index(request):
    return render(request,'index.html')
def portfolio(request):
    return render(request,'portfolio.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Contact Sent Successfully!')
    return render(request,'contact.html')
def testimonial(request):
    return render(request,'testimonial.html')