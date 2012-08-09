from django.conf.urls import patterns, include, url
from core.views import main, members, join, contact

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gnu_clan.views.home', name='home'),
    # url(r'^gnu_clan/', include('gnu_clan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main),
    url(r'^home$', main),
    url(r'^members$', members),
    url(r'^join$', join),
    url(r'^contact$', contact),
)
