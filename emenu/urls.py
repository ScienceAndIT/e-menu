from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'emenu_app.views.index', name='index'),
    url(r'^add_error/$', 'emenu_app.views.add_error', name='add_error'),
    url(r'^menu/(?P<menu_name_url>\w+)/$', 'emenu_app.views.menu', name='menu'),
    url(r'^robots\.txt$', include('robots.urls')),
    # url(r'^emenu/', include('emenu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
