from django.conf.urls import patterns, include, url
from django.contrib import admin

#from main.views import upload_photo

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ocrbackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'main.views.upload_photo', name='upload-photo')
)
