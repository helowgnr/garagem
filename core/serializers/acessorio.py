from rest_framework.serializers import ModelSerializer

from core.models import acessorio

class acessorioSerializer(ModelSerializer):
    class Meta:
        model = acessorio
        fields = "__all__"