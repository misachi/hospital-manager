from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Patients' Details
@python_2_unicode_compatible
class ParentRegistration(models.Model):
    parent_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name + '\t' + self.middle_name + '\t' + self.last_name

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

    @staticmethod
    def get_parent_details(_id):
        parent_ = ParentRegistration.objects.filter(parent_id=_id)
        return parent_


@python_2_unicode_compatible
class ChildRegistration(models.Model):
    child_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(ParentRegistration)
    name = models.CharField(max_length=100)
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

    @staticmethod
    def get_child_details(name):
        child_ = ChildRegistration.objects.filter(name=name)
        return child_

    # method extracts parent using the parent ID number
    @staticmethod
    def get_parent_if_child(name):
        # get parent id by spanning child registration model
        _id = ChildRegistration.objects.filter(name=name).values('parent')

        # Using the returned parent id to get parent details
        parents_ = ChildRegistration.objects.filter(parent__parent_id=_id)
        return parents_


@python_2_unicode_compatible
class InsuranceDetails(models.Model):
    member_id = models.CharField(primary_key=True, max_length=100)
    insurance_name = models.CharField(max_length=30)
    parent = models.ForeignKey(ParentRegistration)
    allergy_details = models.CharField(max_length=500)
    visit_type = models.CharField(max_length=10)

    def __str__(self):
        return self.insurance_name + '\t' + str(self.parent.first_name)

    @staticmethod
    def store_insurance_data(
            _id,
            i_name,
            pid,
            allergy,
            visit):
        pid_ = ParentRegistration.objects.get(parent_id=pid)
        InsuranceDetails.objects.create(
            member_id=_id,
            insurance_name=i_name,
            parent=pid_,
            allergy_details=allergy,
            visit_type=visit,
        )

    @staticmethod
    def get_insurance_details(_id):
        insurance = InsuranceDetails.objects.filter(parent__parent_id=_id)
        return insurance


@python_2_unicode_compatible
class ParentDiagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(ParentRegistration)
    tests = models.CharField(max_length=500)
    specimen = models.CharField(max_length=30)
    lab_test = models.CharField(max_length=20)
    time_to_results = models.DateField()

    @staticmethod
    def create_diagnosis(
            parent,
            test,
            specimen,
            lab,
            time):
        parent_obj = ParentRegistration.objects.get(parent_id=parent)
        ParentDiagnosis.objects.create(
            parent=parent_obj,
            tests=test,
            specimen=specimen,
            lab_test=lab,
            time_to_results=time
        )

    @staticmethod
    def get_parent_diagnosis(_id):
        diagnosis_ = ParentDiagnosis.objects.filter(parent__parent_id=_id)
        return diagnosis_


@python_2_unicode_compatible
class ChildDiagnosis(models.Model):
    diagnosis_id = models.AutoField(primary_key=True)
    child = models.ForeignKey(ChildRegistration)
    tests = models.CharField(max_length=500)
    specimen = models.CharField(max_length=30)
    lab_test = models.CharField(max_length=20)
    time_to_results = models.DateField()

    @staticmethod
    def create_diagnosis(
            child,
            test,
            specimen,
            lab,
            time):
        ChildDiagnosis.objects.create(
            child=child,
            tests=test,
            specimen=specimen,
            lab_test=lab,
            time_to_results=time
        )

    @staticmethod
    def get_diagnosis(name):
        child_ = ChildRegistration.objects.filter(name=name).values('child_id')
        diagnosis_ = ChildDiagnosis.objects.filter(child__child_id=child_)
        return diagnosis_
