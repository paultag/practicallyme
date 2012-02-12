from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('practicallyme.me.views',
    url(r'^login/',    'me_login',       name='me_login' ),
    url(r'^logout/',   'me_logout',      name='me_logout' ),
    url(r'^do_login/', 'me_login_gate',  name='me_login_gate' ),
    url(r'^do_edit/',  'me_edit_update', name='me_edit_update' ),
    url(r'^edit/',     'me_edit',        name='me_edit' ),
)
