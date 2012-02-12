from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404

from practicallyme.me.models import Page

def index(request):
    return render(request, "index.html", {} )

def view_person(request, name):
    owner  = User.objects.filter( username=name )
    lusers = Page.objects.filter( owner=owner )

    if len(lusers) <= 0:
        raise Http404
    luser  = lusers[0]
    owner  = owner[0]

    return render(request, "view.html", {
        "page" : luser,
        "user" : owner
    })
