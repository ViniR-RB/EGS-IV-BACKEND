from rest_framework import viewsets

from .models import *
from .serializers import *


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer