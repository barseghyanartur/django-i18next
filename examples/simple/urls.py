from django.conf.urls import patterns, include, url

from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    # foo URLs:
    url(r'^foo/', include('foo.urls')),

    url(r'^$', TemplateView.as_view(template_name='home/base.html')),
    )

# Serving media and static in debug/developer mode.
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
