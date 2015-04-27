from django.conf.urls import patterns, url
from curves import views

urlpatterns = patterns('',
	#main view
	url(r'^$', views.index, name = 'index'),

	#dept view
	url(r'^(?P<cdept>[A-Za-z]{3,3})/$', views.deptView, name = 'deptView'), 

	#dept-specific view
	url(r'^(?P<cdept>[A-Za-z]{3,3})/(?P<ctime>(F|S)\d{4,4})/$', views.deptSpecificView, name = 'deptSpecificView'), 

	#prof-specific view
	url(r'^prof/(?P<cprof>[^\+]+)/(?P<ctime>(F|S)\d{4,4})/$', views.profSpecificView, name = 'profSpecificView'),

	#professor view
	url(r'^prof/(?P<cprof>[^\+]+)/$', views.profView, name = 'profView'),

	#course view
	url(r'^(?P<cdept>([A-Za-z]{3}\+)*[A-Za-z]{3})/(?P<cnum>(\d{3}[A-Z]?\+)*\d{3}[A-Z]?)/$', views.courseView, name = 'courseView'),

	#course specific view
	url(r'^(?P<cdept>([A-Za-z]{3}\+)*[A-Za-z]{3})/(?P<cnum>(\d{3}[A-Z]?\+)*\d{3}[A-Z]?)/(?P<ctime>(F|S)\d{4,4})/$', views.courseSpecificView, name = 'courseSpecificView'),

	# new mapping
	url(r'^add_data/$', views.add_data, name='add_data'),

	#after data has been added
	url(r'^after_data/$', views.after_data, name = 'after_data'),

	#intermediary url for search queries
	url(r'^search/$', views.search),

	#compare departments
	url(r'^compdept/(?P<cdept1>[A-Za-z]{3,3})/(?P<cdept2>[A-Za-z]{3,3})/$', views.comparedeptView, name = 'comparedeptView'),

	#compare courses
	url(r'^compcourse/(?P<cdept1>([A-Za-z]{3}\+)*[A-Za-z]{3})/(?P<cnum1>(\d{3}[A-Z]?\+)*\d{3}[A-Z]?)/(?P<cdept2>([A-Za-z]{3}\+)*[A-Za-z]{3})/(?P<cnum2>(\d{3}[A-Z]?\+)*\d{3}[A-Z]?)/$', views.comparecourseView, name = 'comparecourseView'),

	#compare professors
	url(r'^compprof/(?P<cprof1>[^\+]+)/(?P<cprof2>[^\+]+)/$', views.compareProfView, name = 'compareProfView')



)