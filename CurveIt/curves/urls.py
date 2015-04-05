from django.conf.urls import patterns, url
from curves import views

urlpatterns = patterns('',
	#main view
	url(r'^$', views.index, name = 'index'),

	#dept view
	url(r'^(?P<cdept>[A-Za-z]{3,3})/$', views.deptView, name = 'deptView'), 

	#professor view
	url(r'^prof/(?P<cprof>[A-Za-z]+)/$', views.profView, name = 'profView'),

	#class view
	#will show a class and link to course specifics for all semesters class has been offered
	#ommitted for now since not critical to rudimentary functionality

	#course specific view
	url(r'^(?P<cdept>[A-Za-z]{3,3})/(?P<cnum>\d{3,3})/(?P<ctime>(F|S)\d{4,4})/$', views.courseSpecificView, name = 'courseSpecificView'),

	# new mapping
	url(r'^add_data/$', views.add_data, name='add_data')

)