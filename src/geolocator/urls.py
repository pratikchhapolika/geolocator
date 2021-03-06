from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'geolocator.views.main_home', name='home'),
    url(r'^search_location/$', 'geolocator.views.location', name='search_location'), 
    url(r'^search_place/$', 'geolocator.views.home', name='search_place'),   # views.home is searching by place
    url(r'^search_place/location/(?P<id>[a-zA-Z0-9_.-]+)/$', 'locations.views.single_location', name='single_location'),
    url(r'^search_location/location/(?P<id>[a-zA-Z0-9_.-]+)/$', 'locations.views.single_location', name='single_location'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
