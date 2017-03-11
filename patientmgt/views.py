from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from patientmgt.forms import RegistrationForm
from patientmgt.models import (
    ParentRegistration,
    ChildRegistration,
    InsuranceDetails,
    Diagnosis,
)


@login_required(login_url='login')
def parent_details(request):
    if request.method == 'POST':
        _id = request.POST.get('_id')
        fname = request.POST('fname')
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

        ChildRegistration.create_parent(
            parent,
            fname,
            mname,
            lname,
            mail_no,
            mobile_no,
            birthday)
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

    return render(request, "patientmgt/insurance.html", {})


@login_required(login_url='login')
def diagnosis(request):
    pass


@login_required(login_url='login')
def search_person(request):
    pass


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

            return redirect('/pa/')
        else:
            return render(request, 'patientmgt/register.html', {'form': user_form})
    else:
        user_form = RegistrationForm()

    return render(request, 'patientmgt/register.html', {'form': user_form})

