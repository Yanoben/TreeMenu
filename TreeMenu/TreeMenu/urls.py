from django.contrib import admin
from django.urls import path
from Tree import urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
