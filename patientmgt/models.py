from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


# Patients' Details
@python_2_unicode_compatible
class ParentRegistration(models.Model):
    parent_id = models.CharField(primary_key=True, max_length=8)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    @staticmethod
    def create_parent(_id,
                      fname,
                      mname,
                      lname,
                      mail_no,
                      mobile_no,
                      birthday):
        ParentRegistration.objects.create(parent_id=_id,
                                               first_name=fname,
                                               middle_name=mname,
                                               last_name=lname,
                                               email=mail_no,
                                               mobile_number=mobile_no,
                                               date_of_birth=birthday)


@python_2_unicode_compatible
class ChildRegistration(models.Model):
    child_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(ParentRegistration)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    @staticmethod
    def create_child(_id,
                      fname,
                      mname,
                      lname,
                      mail_no,
                      mobile_no,
                      birthday):
        ChildRegistration.objects.create(parent_id=_id,
                                               first_name=fname,
                                               middle_name=mname,
                                               last_name=lname,
                                               email=mail_no,
                                               mobile_number=mobile_no,
                                               date_of_birth=birthday)



@python_2_unicode_compatible
class InsuranceDetails(models.Model):
    member_id = models.CharField(primary_key=True, max_length=100)
    insurance_name = models.CharField(max_length=30)
    parent = models.ForeignKey(ParentRegistration)
    allergy_details = models.CharField(max_length=500)
    visit_type = models.CharField(max_length=10)

    @staticmethod
    def store_insurance_data(
            _id,
            i_name,
            pid,
            allergy,
            visit):
        InsuranceDetails.objects.create(
            member_id=_id,
            insurance_name=i_name,
            parent=pid,
            allergy_details=allergy,
            visit_type=visit,
        )


@python_2_unicode_compatible
class Diagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    tests = models.CharField(max_length=500)
    specimen = models.CharField(max_length=30)
    lab_test = models.CharField(max_length=20)
    time_to_results = models.DateField()

    @staticmethod
    def create_diagnosis(
            _id,
            test,
            specimen,
            lab,
            time):
        Diagnosis.objects.create(
            diagnosis_id=_id,
            tests=test,
            specimen=specimen,
            lab_test=lab,
            time_to_results=time
        )


@python_2_unicode_compatible
class SearchDisplay(models.Model):
    parent = models.ForeignKey(ParentRegistration)
    child = models.ForeignKey(ChildRegistration)
    diagnosis = models.ForeignKey(Diagnosis)
    insurance = models.ForeignKey(InsuranceDetails)

    # method extracts parent using the parent ID number
    @staticmethod
    def get_parent_if_child(_id):
        parents_ = SearchDisplay.objects.filter(parentregistration__parent_id=_id)
        return parents_

    @staticmethod
    def get_insurance_details(_id):
        insurance = SearchDisplay.objects.filter(insurancedetails__parentregistration__parent_id=_id)
        return insurance

    @staticmethod
    def get_diagnosis(_id):
        diagnosis_ = SearchDisplay.objects.filter(diagnosis__parentregistration__parent_id=_id)
        return diagnosis_
