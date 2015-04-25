from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CurveIt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include ('curves.urls', namespace = "curves")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/', 'django_cas_ng.views.login'), 
    url(r'logout/$', 'django_cas_ng.views.logout'),
    url(r'^.*$', 'curves.views.handler404'),
    url(r'^autocomplete/', include('autocomplete_light.urls'))
)
handler404 = 'curves.views.handler404'
