from django.contrib import admin
from django.urls import include, path

from boxes.views import index

urlpatterns = [
    path("", index, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("boxes.urls")),
]
