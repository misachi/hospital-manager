from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from patientmgt.forms import RegistrationForm
from patientmgt.models import (
    ParentRegistration,
    ChildRegistration,
    InsuranceDetails,
    ParentDiagnosis,
    ChildDiagnosis,
)


@login_required(login_url='login')
def parent_details(request):
    if request.method == 'POST':
        _id = request.POST.get('_id')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        mail_no = request.POST.get('mail_no')
        mobile_no = request.POST.get('mobile')
        birthday = request.POST.get('bday')

        ParentRegistration.create_parent(
            _id,
            fname,
            mname,
            lname,
            mail_no,
            mobile_no,
            birthday)
        return HttpResponseRedirect('/patient/insurance')

    return render(request, "patientmgt/parent_detail.html", {})


@login_required(login_url='login')
def child_details(request):
    if request.method == 'POST':
        parent = request.POST.get('pid')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        lname = request.POST.get('lname')
        mail_no = request.POST.get('mail_no')
        mobile_no = request.POST.get('mobile')
        birthday = request.POST.get('bday')

        ChildRegistration.create_child(
            parent,
            fname,
            mname,
            lname,
            mail_no,
            mobile_no,
            birthday)
        return HttpResponseRedirect('/patient/insurance')
    return render(request, "patientmgt/child_detail.html", {})


@login_required(login_url='login')
def insurance_details(request):
    if request.method == 'POST':
        insurance_id = request.POST.get('insurance')
        insurance_name = request.POST.get('iname')
        parent_id = request.POST.get('pid')
        allergy_  = request.POST.get('allergy')
        visit_type = request.POST.get('patient')

        if visit_type in ["inpatient", "outpatient"]:
            InsuranceDetails.store_insurance_data(
                insurance_id,
                insurance_name,
                parent_id,
                allergy_,
                visit_type
            )
            return HttpResponseRedirect('patient/diagnosis')

    return render(request, "patientmgt/insurance.html", {})


@login_required(login_url='login')
def parent_diagnosis(request):
    if request.method == 'POST':
        parent = request.POST.get('parent')
        tests = request.POST.get('test')
        specimen = request.POST.get('specimen')
        lab_test = request.POST.get('lab')
        get_time = request.POST.get('time')
        set_time = parse_date(get_time)

        ParentDiagnosis.create_diagnosis(
            parent,
            tests,
            specimen,
            lab_test,
            set_time,
        )
    return render(request, 'patientmgt/diagnosis.html', {})


@login_required(login_url='login')
def search(request):
    user = request.user
    srch_term = request.POST.get('srch-term')
    result_parent, result_child, result_child_diagnosis = [], [], []

    if type(srch_term) == str:
        child_parent = ChildRegistration.get_parent_if_child(srch_term)
        details_for_child = ChildRegistration.get_child_details(srch_term)
        diagnosis_for_child = ChildDiagnosis.get_diagnosis(srch_term)
        result_child.append(details_for_child)
        result_parent.append(child_parent)
        result_child_diagnosis.append(diagnosis_for_child)

    parent_diagnosis_ = ParentDiagnosis.get_parent_diagnosis(srch_term)
    insurance = InsuranceDetails.get_insurance_details(srch_term)
    return render(request, 'patientmgt/display.html', {
        'user': user,
        'insurance': insurance,
        'parent_diagnosis': parent_diagnosis_,
        'child_diagnosis': result_child_diagnosis,
        'child_reg_details': result_child,
        'child_parent_insurance': result_parent
    })


def doctor_register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password')

            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            user = authenticate(username=username, password=password)
            login(request, user)

            return HttpResponseRedirect('patient/parent')
        else:
            return render(request, 'patientmgt/register.html', {'form': user_form})
    else:
        user_form = RegistrationForm()

    return render(request, 'patientmgt/register.html', {'form': user_form})

