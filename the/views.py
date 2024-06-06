from django.shortcuts import render,redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login as log, logout as lo
from django.contrib.auth.models import User
from .models import Utente, The, Recensione, Preferito
from .forms import addThe

from datetime import datetime

import logging
# Create your views here.

def dettaglio(request,id):
    if request.method=="GET":
        the = The.objects.get(id=id)
        user = request.user
        recensioni = Recensione.objects.filter(id_the=the.id)
        preferito = Preferito.objects.filter(id_utente=user.id, id_the=the.id)
        context = {
            "the":the,
            "user": user,
            "recensioni": recensioni,
            "preferito": preferito
            }
        return render(request, 'the/dettaglio.html', context)
    
    elif request.method=="POST":
        
        the = The.objects.get(id=id)
        user = request.user
        
        if 'add-rece' in request.POST:
            commento = request.POST['commento-input']
            voto = request.POST['starsNumber']
            data = datetime.now()
            Recensione.objects.create(id_utente=user, id_the=the,commento=commento, voto=voto, data=data)
            recensioni = Recensione.objects.filter(id_the=the.id)
            preferito = Preferito.objects.filter(id_utente=user.id, id_the=the.id)
            
            
            context = {
                "the":the,
                "user": user, 
                "recensioni": recensioni,
                "preferito": preferito
                }
            return render(request, 'the/dettaglio.html', context)
            
        elif 'add-prefe' in request.POST:
            Preferito.objects.create(id_utente=user, id_the=the)
            
            recensioni = Recensione.objects.filter(id_the=the.id)
            preferito = Preferito.objects.filter(id_utente=user.id, id_the=the.id)
            
            context = {
                "the":the,
                "user": user, 
                "recensioni": recensioni,
                "preferito": preferito
                }
            return render(request, 'the/dettaglio.html', context)
        
        elif 'preferiti' in request.POST:
            query = Preferito.objects.filter(id_utente=user)
            thes = []
            for i in query:
                thes.append(i.id_the)
            context = {"thes": thes}
            return render(request, 'the/home.html', context)
        
        elif 'del-prefe' in request.POST:
            Preferito.objects.filter(id_utente=user.id, id_the=the.id).delete()
            
            recensioni = Recensione.objects.filter(id_the=the.id)
            preferito = Preferito.objects.filter(id_utente=user.id, id_the=the.id)
            
            
            context = {
                "the":the,
                "user": user, 
                "recensioni": recensioni,
                "preferito": preferito
                }
            return render(request, 'the/dettaglio.html', context)
            
        
        
        
        
        

def addthe(request):
    if request.method=="GET":
        form = addThe()
    
    elif request.method=="POST":
        form = addThe(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(home)
        
        
    return render(request, 'the/addthe.html', {'form': form})


def home(request):
    user=request.user
    if request.method=="GET":
        thes = The.objects.all()
        context = {"thes": thes}
        return render(request, "the/home.html", context)
    elif request.method=="POST":
        if 'search' in request.POST:
            nome = request.POST['search']
            thes = The.objects.filter(provenienza=nome)
            context = {
                "thes": thes,
                "search": True}
        elif 'preferiti' in request.POST:
            query = Preferito.objects.filter(id_utente=user)
            thes = []
            for i in query:
                thes.append(i.id_the)
            context = {
                "thes": thes,
                "search": False}
        return render(request, "the/home.html", context)


def login(request):
    lo(request)
    if request.method=="GET":
        return render(request, 'the/login.html')
    
    elif request.method=="POST":
        username = request.POST['username-input']
        password = request.POST['password-input']
        user = authenticate(username=username, password=password)
        if user is not None:
            log(request, user)
            return redirect(home)
        else:
            return redirect(login)
    


def signup(request):
    if request.method=="GET":
        return render(request, 'the/signup.html')
    
    elif request.method=="POST":
        username = request.POST['username']
        email =  request.POST['email']
        type = request.POST['type']
        password = request.POST['password']
        if type!='user' and type!='admin':
            return render(request, 'the/signup.html', context={"valid": False})
        else:  
            user = User.objects.create_user(username=username, email=email, password=password)
            Utente.objects.create(user=user, tipo=type)
            return redirect(login)
    
    
    
def logout(request):
    lo(request)
    thes = The.objects.all()
    context = {"user": request.user,
               "thes": thes}
    return render(request, 'the/home.html', context)
        