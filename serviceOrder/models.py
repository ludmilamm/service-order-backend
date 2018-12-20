from django.db import models

class City(models.Model):
    description = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

class Neighborhood(models.Model):
    description = models.CharField(max_length=50)
    city = models.ForeignKey(City, models.DO_NOTHING)

class Patient(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField(auto_now=False)
    gender = models.CharField(max_length=1)
    address = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, models.DO_NOTHING)

class Specialty(models.Model):
    description = models.CharField(max_length=50)

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialty = models.ForeignKey(Specialty, models.DO_NOTHING)

class CollectionPoint(models.Model):
    description = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    neighborhood = models.ForeignKey(Neighborhood, models.DO_NOTHING)

class HealthInsurance(models.Model):
    description = models.CharField(max_length=50)

class Sector(models.Model):
    description = models.CharField(max_length=50)

class Exam(models.Model):
    description = models.CharField(max_length=100)
    biologicalMaterial = models.CharField(max_length=50)
    deadline = models.IntegerField(default=0)
    sector = models.ForeignKey(Sector, models.DO_NOTHING)

class HealthInsuranceExamPrice(models.Model):
    healthInsurance = models.ForeignKey(HealthInsurance, models.DO_NOTHING)
    exam = models.ForeignKey(Exam, models.DO_NOTHING)
    price = models.DecimalField(max_digits=8, decimal_places=2)

class ServiceOrder(models.Model):
    date = models.DateField(auto_now=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    healthInsurance = models.ForeignKey(HealthInsurance, models.DO_NOTHING)
    collectionPoint = models.ForeignKey(CollectionPoint, models.DO_NOTHING)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING)

class ServiceOrderExam(models.Model):
    WAITING = "waiting"
    PROCESSING = "processing"
    CANCELED = "canceled"
    AVAILABLE = "available"
    TAKEN = "taken"
    STATUS_CHOICES = (
        (WAITING, "Waiting"),
        (PROCESSING, "Processing"),
        (CANCELED, "Canceled"),
        (AVAILABLE, "Available"),
        (TAKEN, "Taken")
    )
    serviceOrder = models.ForeignKey(ServiceOrder, models.CASCADE, related_name='exams')
    exam = models.ForeignKey(Exam, models.CASCADE)
    resultDate = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=WAITING)