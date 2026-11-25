from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),

    # Project applications
    path("", include("apps.core.urls")),
    path("accounts/", include("apps.accounts.urls")),
    path("news/", include("apps.news.urls")),
    path("articles/", include("apps.articles.urls")),
    path("blogs/", include("apps.blogs.urls")),
    path("forum/", include("apps.forum.urls")),
    path("events/", include("apps.events.urls")),
    path("messaging/", include("apps.messaging.urls")),
    path("notifications/", include("apps.notifications.urls")),
]


# Serve uploaded media files during development only.

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
