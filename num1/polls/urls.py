from django.conf.urls import *
from polls import views

urlpatterns = (
	url(r'^$',views.index,name='index'),
	url(r'^names/(?P<name>.+)/$',views.main),
)
