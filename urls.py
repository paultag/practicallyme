from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

import practicallyme.me.urls

admin.autodiscover()

urlpatterns = patterns('practicallyme.views',
    url(r'^me/',      include(practicallyme.me.urls)),
    url(r'^admin/',   include(admin.site.urls)),
    # OK. Big stuff is out of the way.
    url(r'^$',              'index',      name='index'       ),
    url(r'^(?P<name>.*)/$', 'view_person', name='view_person' ),
)
