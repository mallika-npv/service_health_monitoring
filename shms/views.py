from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import service, days
from .forms import CheckboxForm
from django.db.models import Q
import random 
from django.core.mail import send_mail

def update_service_statuses(request):
    services = service.objects.all()
    s = service.objects.all()[random.randint(0, 4)]
    if s.status:
        x = [True,True,True,False]
        s.status = random.choice(x)
        s.save()
    else:
        s.status = True
        s.save()   
    for i in services:
        if not i.status:
            i.time += 10000
            i.save()
            if i.time >= 60000:
                subject = 'Down-time for services' 
                message = f'the downtime for the service {i.name} is currently 1 minute'
                from_email = 'mallikanpv@gmail.com'
                recipient_list = [request.user.email]
                send_mail(subject, message, from_email, recipient_list)
    service_statuses = [{'name': s.name, 'status': s.status}]
    return JsonResponse({'services': service_statuses})

def dashboard(request):
    if request.method == "POST":
        form = CheckboxForm(request.POST)
        if form.is_valid():
            query = Q()  
            if form.cleaned_data['google']:
                query |= Q(webs='google')
            if form.cleaned_data['facebook']:
                query |= Q(webs='facebook')
            if form.cleaned_data['amazon']:
                query |= Q(webs='amazon')
            if form.cleaned_data['twitter']:
                query |= Q(webs='twitter')

            if form.cleaned_data['selected_date']:
                selected_date = form.cleaned_data['selected_date']
                query &= Q(date=selected_date)
            else:
                items = days.objects.filter(query)

            if form.cleaned_data['dt']:
                selected_dt = form.cleaned_data['dt']
                query &= Q(dt__gte = selected_dt)
            else:
                items = days.objects.filter(query)

            items = days.objects.filter(query)
            services = service.objects.all()
            return render(request, 'shms/dashboard.html', {'items': items, 'services': services})
    else:
        services = service.objects.all()
        return render(request, 'shms/dashboard.html', {'services': services})
        
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "shms/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "shms/login.html")

def logout_view(request):
    logout(request)
    return render(request, "shms/login.html", {
        "message" : "logged out."
    })

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "shms/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return render(request, "shms/register.html")