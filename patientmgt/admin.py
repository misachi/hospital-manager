from django.contrib import admin
from patientmgt.models import (
    ParentRegistration,
    ChildRegistration,
    InsuranceDetails,
    Diagnosis
)

admin.site.register(ParentRegistration)
admin.site.register(ChildRegistration)
admin.site.register(InsuranceDetails)
admin.site.register(Diagnosis)
