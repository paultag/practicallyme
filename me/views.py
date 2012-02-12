from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from practicallyme.me.models import Page
from practicallyme.me import config

def isLoggedIn(request):
    return request.session.get('cur_user', False)

def get_page(user):
    try:
        page = Page.objects.get(owner=user)
    except Page.DoesNotExist:
        page = Page(
            owner=user
        )
        page.save()
    return page

def me_login_gate(request):
    if isLoggedIn(request):
        return redirect( "me_edit" )

    if not "uname" in request.POST or not "passw" in request.POST:
        return redirect( "me_login" )

    username = request.POST["uname"]
    password = request.POST["passw"]

    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            request.session['cur_user'] = user.username
            return redirect( "me_edit" )
        else:
            return redirect( "me_login" )
    except User.DoesNotExist:
        return redirect( "index" )

def me_login(request):
    if isLoggedIn(request):
        return redirect( "me_edit" )
    return render( request, "me/login.html", {})

def me_logout(request):
    request.session.clear()
    return redirect( "index" )

@require_POST
def me_edit_update(request):
    if not isLoggedIn(request):
        return redirect( "me_login" )
    # validate post
    keys = config.get_fields()

    for key in keys:
        if not key in request.POST:
            # set warning
            return redirect( "me_edit" )

    user = User.objects.get(
        username=request.session['cur_user']
    )
    page = get_page(user)
    p = request.POST

    user.email      = p['priv_email']
    user.first_name = p['first_name']
    user.last_name  = p['last_name']
    page.font       = p['font']
    page.title      = p['title']
    page.background = p['background']
    page.website    = p['website']
    page.email      = p['pub_email']
    page.blurb      = p['blurb']

    page.save()
    user.save()

    return redirect( "view_person", name=request.session['cur_user'] )

def me_edit(request):
    if not isLoggedIn(request):
        return redirect( "me_login" )

    user = User.objects.get(username=request.session['cur_user'])
    page = get_page( user )
    fields = config.get_field_dict( user, page )
    order  = config.get_fields()

    return render( request, "me/edit.html", {
        "user"        : user,
        "page"        : page,
        "field_order" : order,
        "fields"      : fields
    })
