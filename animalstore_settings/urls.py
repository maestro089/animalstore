from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [  # noqa
    path("admin/", admin.site.urls),
    path("admin-panel/", include("admin_panel.urls")),
    path("", include("store.urls")),
    path("news/", include("news.urls")),
    path("clients/", include("clients.urls")),
    path("cart/", include("cart.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
