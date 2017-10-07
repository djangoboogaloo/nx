from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static





from django.contrib.auth import views as auth_views


from Account import views as core_views




urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^$', index,name='home'),
    # url(r'^health$', health),

    # url(r'^account/', include('Account.urls'), namespace='account'),
    url(r'^tai-khoan/',include('Account.urls',namespace='account')),

    url(r'^thong-bao/', include("blog.urls",namespace='blog')),
    #stream balance











    #only use for active...and so on

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
