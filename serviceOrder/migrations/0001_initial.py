# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-18 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CollectionPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('biologicalMaterial', models.CharField(max_length=50)),
                ('deadline', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='HealthInsurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HealthInsuranceExamPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Exam')),
                ('healthInsurance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.HealthInsurance')),
            ],
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.City')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=50)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('collectionPoint', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.CollectionPoint')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Doctor')),
                ('healthInsurance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.HealthInsurance')),
                ('patitent', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOrderExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultDate', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Exam')),
                ('serviceOrder', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.ServiceOrder')),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='exam',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Sector'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Specialty'),
        ),
        migrations.AddField(
            model_name='collectionpoint',
            name='neighborhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='serviceOrder.Neighborhood'),
        ),
    ]
