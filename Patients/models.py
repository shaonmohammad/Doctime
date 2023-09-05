from django.db import models
from Doctors.models import Doctor


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    address = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ("Heart Patients", "Heart Patients"),
        ("Liver Patients", "Liver Patients"),

    ])

    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='patients', null=True)

    def __str__(self):
        return self.name
