from django.contrib import admin
from .models import Patients, Doctors, Specialty, PaymentStatus, Appointments, Billing, Diagnosis
# Register your models here.

admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Specialty)
admin.site.register(PaymentStatus)
admin.site.register(Appointments)
admin.site.register(Billing)
admin.site.register(Diagnosis)