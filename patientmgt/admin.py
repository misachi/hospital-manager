from django.contrib import admin
from patientmgt.models import (
    ParentRegistration,
    ChildRegistration,
    InsuranceDetails,
    ParentDiagnosis,
    ChildDiagnosis,
)

admin.site.register(ParentRegistration)
admin.site.register(ChildRegistration)
admin.site.register(InsuranceDetails)
admin.site.register(ParentDiagnosis)
admin.site.register(ChildDiagnosis)
