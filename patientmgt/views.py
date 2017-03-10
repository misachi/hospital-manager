from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from patientmgt.forms import RegistrationForm
from patientmgt.models import ParentRegistration


def parent_details(request):
    if request.method == 'POST':
        _id = request.POST['parent_id']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        mail_no = request.POST['mail_no']
        mobile_no = request.POST['mobile']
        birthday = request.POST['birthday']

        ParentRegistration.create_parent(_id, fname, mname, lname, mail_no, mobile_no, birthday)
    return render(request, "patientmgt/parent_detail.html", {})


def child_details(request):
    pass


def insurance_details(request):
    pass


def diagnosis(request):
    pass


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

