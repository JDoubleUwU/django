from django.db import models

# Create your models here.
class Patients(models.Model):
    patient_ID = models.IntegerField(primary_key=True)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.patient_ID} - {self.first_name} - {self.last_name} - {self.date_of_birth}"

class Specialty(models.Model):
    specialty_ID = models.IntegerField(primary_key=True)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.specialty_ID} - {self.specialty}"

class Doctors(models.Model):
    doctor_ID = models.IntegerField(primary_key=True)
    first_name = models.TextField(max_length=255)
    last_name = models.TextField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.doctor_ID} - {self.first_name} - {self.last_name} - {self.specialty}"

class Appointments(models.Model):
    appointment_ID = models.IntegerField(primary_key=True)
    patient_ID = models.ForeignKey(Patients, on_delete=models.DO_NOTHING)
    doctor_ID = models.ForeignKey(Doctors, on_delete=models.DO_NOTHING)
    appoinmentDate = models.DateTimeField()

    def __str__(self):
        return f"{self.appointment_ID} - {self.patient_ID} - {self.doctor_ID} - {self.appoinmentDate}"

class Diagnosis(models.Model):
    patient_ID = models.ForeignKey(Patients, on_delete=models.DO_NOTHING)
    doctor_ID = models.ForeignKey(Doctors, on_delete=models.DO_NOTHING)
    diagnosis = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.patient_ID} - {self.doctor_ID} - {self.diagnosis}"

class PaymentStatus(models.Model):
    paymentstatus_id = models.IntegerField(primary_key=True)
    paymentstatus = models.TextField(max_length=20)

    def __str__(self):
        return f"{self.paymentstatus_id} - {self.paymentstatus}"

class Billing(models.Model):
    billing_ID = models.IntegerField(primary_key=True)
    total_amount = models.IntegerField()
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.billing_ID} - {self.total_amount} - {self.payment_status}"