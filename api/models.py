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


class Integrations(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Inspector(models.Model):
    createdAt = models.DateTimeField()
    name = models.CharField(max_length=200)
    availableIntegrations = models.ManyToManyField(Integrations)

    def __str__(self):
        return self.name


class Inspections(models.Model):
    createdAt = models.DateTimeField()
    city = models.CharField(max_length=200)
    scheduledDate = models.DateTimeField()
    inspectorId = models.ForeignKey(Inspector, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.company


class Items(models.Model):
    createdAt = models.DateTimeField()
    isIssue = models.IntegerField(default=0)
    severity = models.IntegerField(default=0)
    label = models.CharField(max_length=200)
    position = models.IntegerField(default=0)
    inspectionId = models.ForeignKey(Inspections, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
