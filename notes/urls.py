"""URLs"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from ratelimit.exceptions import Ratelimited

urlpatterns = [
    path("", include("news.urls")),
    path("", include("accounts.urls")),
    path("digest/", include("emaildigest.urls")),
    path("admin/", admin.site.urls),
    path("auth/", include("magiclink.urls", namespace="magiclink")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns


def handler403(_, exception=None):
    """Too fast!"""
    if isinstance(exception, Ratelimited):
        return HttpResponse(
            "<img src='https://http.cat/429.jpg'><br>Estás refrescando muy rápido ¡Intenta de nuevo!",
            status=429,
        )
    return HttpResponseForbidden("Forbidden")
