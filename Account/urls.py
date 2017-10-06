
from django.conf.urls import  url


from django.contrib.auth import views as auth_views
# from .views import user_view,user_edit,my_profile
from django.conf.urls import url
from django.contrib import admin
from .views import (
	login,
	logout,
	resign,
	)

urlpatterns = [
	# url(r'^$', my_profile, name='my_profiley'),
	# url(r'^edit/$', my_profile, name='edit_my_profiley'),
	# url(r'^(?P<pk>\d+)$', user_view, name='detail'),


	#using system

    url(r'^dang-nhap/$', login, name='login'),
    url(r'^thoat/$', logout,name='logout'),
    url(r'^dang-ky/$', resign,name='resign' ),

]
