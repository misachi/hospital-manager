# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChildDiagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(primary_key=True, serialize=False)),
                ('tests', models.CharField(max_length=500)),
                ('specimen', models.CharField(max_length=30)),
                ('lab_test', models.CharField(max_length=20)),
                ('time_to_results', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ChildRegistration',
            fields=[
                ('child_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceDetails',
            fields=[
                ('member_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('insurance_name', models.CharField(max_length=30)),
                ('allergy_details', models.CharField(max_length=500)),
                ('visit_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ParentDiagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(primary_key=True, serialize=False)),
                ('tests', models.CharField(max_length=500)),
                ('specimen', models.CharField(max_length=30)),
                ('lab_test', models.CharField(max_length=20)),
                ('time_to_results', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ParentRegistration',
            fields=[
                ('parent_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ChildRegistration')),
                ('child_diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ChildDiagnosis')),
                ('insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.InsuranceDetails')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ParentRegistration')),
                ('parent_diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ParentDiagnosis')),
            ],
        ),
        migrations.AddField(
            model_name='parentdiagnosis',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ParentRegistration'),
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
            model_name='childdiagnosis',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patientmgt.ChildRegistration'),
        ),
    ]
