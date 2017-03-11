from django.conf.urls import url
from patientmgt.views import (
    parent_details,
    child_details,
    doctor_register,
    insurance_details,
    diagnosis,
    search,
)

urlpatterns = [
    # url(r'^$', parent_details, name='patientmgt_home'),
    url(r'^register/$', doctor_register, name='patientmgt_register'),
    url(r'^parent/$', parent_details, name='patientmgt_parent'),
    url(r'^child/$', child_details, name='patientmgt_child'),
    url(r'^insurance/$', insurance_details, name='patientmgt_insurance'),
    url(r'^diagnosis/$', diagnosis, name='patientmgt_diagnosis'),
    url(r'^search/$', search, name='patientmgt_search')
]