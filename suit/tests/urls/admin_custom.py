from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

admin.autodiscover()

urlpatterns = [
    # Examples for custom menu
    re_path(r'^foo/bar/', include(admin.site.urls)),
]
