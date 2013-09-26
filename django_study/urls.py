from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_study.views.home', name='home'),
    # url(r'^django_study/', include('django_study.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # ex: /app/
    # url(r'^$', views.index, name='index'),
    # ex: /app/5/
    # url(r'^(?P<user_id>\d+)/$', views.detail, name='detail'),
    # ex: /app/5/results/
    # url(r'^(?P<user_id>\d+)/results/$', views.results, name='results'),
    # ex: /app/5/vote/
    # url(r'^(?P<user_id>\d+)/vote/$', views.vote, name='vote'),
    # ex: /app/
    url(r'^app/current_datetime/', 'app.views.current_datetime', name='current_datetime'),
    url(r'^$', 'app.views.contactus', name='contactus'),
)
