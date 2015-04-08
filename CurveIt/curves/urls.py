from django.conf.urls import patterns, url
from curves import views

urlpatterns = patterns('',
	#main view
	url(r'^$', views.index, name = 'index'),

	#dept view
	url(r'^(?P<cdept>[A-Za-z]{3,3})/$', views.deptView, name = 'deptView'), 

	#professor view
	url(r'^prof/(?P<cprof>[\x00-\x7F]+)/$', views.profView, name = 'profView'),

	#course view
	url(r'^(?P<cdept>([A-Za-z]{3}\+)*[A-Za-z]{3})/(?P<cnum>(\d{3,4}\+)*\d{3,4})/$', views.courseView, name = 'courseView'),

	#course specific view
	url(r'^(?P<cdept>([A-Za-z]{3}\+)*[A-Za-z]{3})/(?P<cnum>(\d{3,4}\+)*\d{3,4})/(?P<ctime>(F|S)\d{4,4})/$', views.courseSpecificView, name = 'courseSpecificView'),

	# new mapping
	url(r'^add_data/$', views.add_data, name='add_data')

)