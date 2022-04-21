from django.http import HttpResponse
from django.template import loader
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from datetime import datetime
import requests

from . import inspectionInspectorSerializer
from api.models import InspectionInspector


class SolarGradeAPI(ListCreateAPIView):
    queryset = InspectionInspector.objects.all()
    serializer_class = inspectionInspectorSerializer.InspectionInspectorSerializer
    permission_classes = (AllowAny,)


class SolarGradeByCompany(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = inspectionInspectorSerializer
    http_method_names = ['get']

    def get_queryset(self):
        company_name = self.request.query_params.get('company_name')
        result = []
        inspectors = requests.get("https://6244305b3da3ac772b0c7854.mockapi.io/fakeSolar/3rdParty/inspectors", timeout=10)
        if inspectors.status_code == 200:
            dataInspectors = inspectors.json()
            inspections = requests.get("https://6244305b3da3ac772b0c7854.mockapi.io/fakeSolar/3rdParty/inspections", timeout=10)
            if inspections.status_code == 200:
                dataInspections = inspections.json()
                for d in dataInspections:
                    for i in dataInspectors:
                        if company_name in i.get('availableIntegrations'):
                            toInsert = InspectionInspector()
                            toInsert.name = f"{d.get('city')} - {d.get('createdAt')}"
                            toInsert.inspectorName = i.get('name')
                            toInsert.itemsOK = len([item for item in d.get('items') if not item.get('isIssue')])
                            toInsert.issuesCriticalCount = len([item for item in d.get('items') if item.get('isIssue') and item.get('severity') < 60])
                            toInsert.issuesWarningCount = len([item for item in d.get('items') if item.get('isIssue') and item.get('severity') >= 60])
                            toInsert.Company = company_name
                            result.append(toInsert)

        template = loader.get_template('polls/details.html')
        return HttpResponse(template.render({'inspections': result}))
