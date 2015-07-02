from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/', include('polls.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
