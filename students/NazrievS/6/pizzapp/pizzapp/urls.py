# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/',
        include(
            (
                'nazrpizza.urls',
                'nazrpizza',
            ),
            namespace='pizzapp',
        ),
    ),
]
