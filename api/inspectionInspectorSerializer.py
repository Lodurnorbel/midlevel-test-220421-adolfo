from rest_framework import  serializers
from api.models import InspectionInspector


class InspectionInspectorSerializer (serializers.ModelSerializer):
    class Meta:
        model = InspectionInspector
        fields = "__all__"