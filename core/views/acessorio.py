from rest_framework.viewsets import ModelViewSet

from core.models import acessorio
from core.serializers import acessorioSerializer


class acessorioViewSet(ModelViewSet):
    queryset = acessorio.objects.all()
    serializer_class = acessorioSerializer