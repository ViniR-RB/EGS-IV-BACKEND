
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from todo.views import *

router = routers.DefaultRouter()

router.register(r'todo', TodoViewSet, basename='todo')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api')
]
