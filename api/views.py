from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import AllowAny

from . import serializer
from api.models import InspectionInspector


class SolarGradeAPI(ListCreateAPIView ):
    queryset = InspectionInspector.objects.all()
    serializer_class = serializer.InspectionInspectorSerializer
    permission_classes = (AllowAny, )
