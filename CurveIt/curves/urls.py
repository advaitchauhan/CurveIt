from django.conf.urls import patterns, url
from curves import views

urlpatterns = patterns('',
	#main view
	url(r'^$', views.index, name = 'index'),

	#dept view
	#url(r'^(?P<cdept>[A-Za-z]{3,3})/$', views.dept, name = 'dept'), 

	#class view

	#course specific view
	url(r'^(?P<cdept>[A-Za-z]{3,3})/(?P<cnum>\d{3,3})/(?P<ctime>(F|S)\d{4,4})$', views.CS, name = 'CS')
)