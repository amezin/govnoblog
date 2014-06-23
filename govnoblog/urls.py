from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'govnoblog.views.userlist', name='userlist'),
    url(r'^user/(?P<username>[^/]+)$', 'govnoblog.views.postlist', name='postlist'),
    url(r'^newpost$', 'govnoblog.views.newpost', name='newpost'),
    url(r'^login$', 'django.contrib.auth.views.login', kwargs={'template_name': 'login.html'}),
    url(r'^logout$', 'django.contrib.auth.views.logout', kwargs={'template_name': 'logged_out.html'}),
    url(r'^admin/', include(admin.site.urls)),
)
