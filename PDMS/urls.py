# PDMS/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("pdms/", include("pdms_app.urls")),
    path("", lambda request: redirect("download_page")),  # redirect root → downloads
]
