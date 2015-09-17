from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic.base import RedirectView
from api.v3.urls import api_v3_docs
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^admin/queue/', include('django_rq.urls')),
    url(r'^admin/task_queue/', include('task_queue.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api', include('api.urls')),
    url(r'^home$', TemplateView.as_view(template_name='home/home.html'),name='home'),
    url(r'^about$', TemplateView.as_view(template_name='home/about.html'),name='about'),
    url(r'', include('two_factor.urls', 'two_factor')),
    url(r'^$',
        RedirectView.as_view(url='/home', permanent=True),
        name='index'),
    (r'^search/', include('haystack.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
