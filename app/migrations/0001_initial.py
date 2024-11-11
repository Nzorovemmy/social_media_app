# Generated by Django 5.1.3 on 2024-11-08 13:44

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
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('enroll_year', models.IntegerField()),
                ('current_GPA', models.IntegerField(blank=True, null=True)),
                ('department', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]