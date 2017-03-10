# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 22:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildRegistration',
            fields=[
                ('child_id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(primary_key=True, serialize=False)),
                ('tests', models.CharField(max_length=500)),
                ('specimen', models.CharField(max_length=30)),
                ('lab_test', models.CharField(max_length=20)),
                ('time_to_results', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceDetails',
            fields=[
                ('member_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('insurance_name', models.CharField(max_length=30)),
                ('allergy_details', models.CharField(max_length=500)),
                ('visit_type', models.CharField(choices=[('IN', 'Inpatient'), ('OUT', 'Outpatient')], default='IN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='ParentRegistration',
            fields=[
                ('parent_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('mobile_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='insurancedetails',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ParentRegistration'),
        ),
        migrations.AddField(
            model_name='childregistration',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ParentRegistration'),
        ),
        migrations.AddField(
            model_name='childregistration',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
