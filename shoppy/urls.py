"""
URL configuration for shoppy project.

... (rest of your docstring)
"""
from django.contrib import admin
from django.urls import path
from home import views

# New imports for media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
]

# This is the crucial part.
# ONLY add this to urlpatterns when in development (settings.DEBUG is True).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)