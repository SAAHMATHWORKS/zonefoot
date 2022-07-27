from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scores.urls')),
    path('account/', include('account.urls')),
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ZONEFOOT6"
admin.site.site_title = "ZONEFOOT6"
admin.site.index_title = "ZONEFOOT6"