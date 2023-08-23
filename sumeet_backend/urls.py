from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

v1_api_urls = [
    path("users/", include("users.urls")),
    path("", include("consultation.urls")),
]

api_urls = [
    path("v1/", include(v1_api_urls)),
]

urlpatterns = [
    path("api/", include(api_urls)),
    path("admin/", admin.site.urls),
    path("", include("telegram_bot.urls"), name="telegram"),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]
