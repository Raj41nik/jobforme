# Generated by Django 5.0.4 on 2024-08-20 19:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('companyName', models.CharField(max_length=200)),
                ('salaryLow', models.IntegerField(default=0)),
                ('salaryHigh', models.IntegerField(default=0)),
                ('applyCount', models.IntegerField(default=0)),
                ('lastDateApply', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passingYear', models.IntegerField()),
                ('YearOfExp', models.ImageField(default=0, upload_to='')),
                ('resume', models.FileField(upload_to='resume/')),
                ('status', models.CharField(choices=[('pendding', 'pendding'), ('selected', 'selected')], default='pendding', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hr.jobpost')),
            ],
        ),
        migrations.CreateModel(
            name='selectCandidateJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hr.candidateapplication')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.jobpost')),
            ],
        ),
    ]
