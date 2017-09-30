# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from django.contrib import messages
from models import Wish


# Route to dashboard -> /wish/
def dashboard(request):
    context = {
        'curUser': User.objects.get(id = request.session['id']),
        'otherUsers': User.objects.exclude(id = request.session['id']),
        'allProducts': Wish.objects.all(),
        'allOtherUsers':[],
        'myProducts' : Wish.objects.filter(products = User.objects.get(id = request.session['id']))
    }

    otherUsers = User.objects.exclude(id = request.session['id'])
    for user in otherUsers:
        if user.id == request.session['id']:
            context['cur_User'].append(user)
        else:
            context['allOtherUsers'].append(user)

    return render(request,'wish_app/dashboard.html', context)

# Route to addProduct -> /wish/addProduct
def addProduct(request):
    return render(request,'wish_app/create.html')

# Route to addProduct -> /wish/create
def create(request):
    if len(request.POST['products']) < 3:
        messages.error(request, 'Product name to short!')
        return redirect('/wish/addProduct')
    else:
        Wish.objects.create(products = request.POST['products'])
    return redirect('/wish/')

def add(request, id):
    return redirect('/wish/')

# Route to remove item -> /wish/remove
def remove(request, id):
    Wish.objects.get(id = id).delete()
    return redirect('/wish/')

# Route to item page -> /wish/item
def item(request, id):
    context = {
    'userWhoadded': User.objects.get(id = request.session['id']),
    'userItems':[],
    }

    userProducts = Wish.objects.all()
    context['userItems'].append(Wish.objects.get(id = id))

    return render(request,'wish_app/item.html',context)

# Route to addProduct -> /wish/logout
def logout(request):
    request.session.flush()
    return redirect('/')
