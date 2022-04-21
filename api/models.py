from django.db import models


class InspectionInspector(models.Model):
    title = models.CharField(max_length=200)
    inspectorName = models.CharField(max_length=200)
    itemsOK = models.IntegerField(default=0)
    issuesWarningCount = models.IntegerField(default=0)
    issuesCriticalCount = models.IntegerField(default=0)
    Company = models.CharField(max_length=200)

    def __str__(self):
        return self.title
