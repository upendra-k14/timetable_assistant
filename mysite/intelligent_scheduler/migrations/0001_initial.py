# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-03 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(choices=[(b'UG1', b'UG1'), (b'UG2', b'UG2'), (b'UG3', b'UG3'), (b'UG4', b'UG4')], default=b'UG1', max_length=4)),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('cid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100)),
                ('cshortname', models.CharField(max_length=6)),
                ('nclasses', models.IntegerField(default=2)),
                ('ntutorials', models.IntegerField(default=2)),
                ('expectedstrength', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='CourseTaken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intelligent_scheduler.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(choices=[(b'UG1', b'UG1'), (b'UG2', b'UG2'), (b'UG3', b'UG3'), (b'UG4', b'UG4')], default=b'UG1', max_length=4)),
                ('branch', models.CharField(choices=[(b'CSE', b'CSE'), (b'ECE', b'ECE')], default=b'CSE', max_length=4)),
                ('course_type', models.CharField(choices=[(b'C', b'Core Course'), (b'FC', b'Flexi Core Course'), (b'ITE', b'IT Elective')], max_length=4)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intelligent_scheduler.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('fshortname', models.CharField(max_length=4)),
                ('isvisiting', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LunchBreak',
            fields=[
                ('batch', models.CharField(choices=[(b'UG1', b'UG1'), (b'UG2', b'UG2'), (b'UG3', b'UG3'), (b'UG4', b'UG4')], default=b'UG1', max_length=4, primary_key=True, serialize=False)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PreferredFacultyHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_day', models.CharField(choices=[(b'SUN', b'Sunday'), (b'MON', b'Monday'), (b'TUE', b'Tuesday'), (b'WED', b'Wednesday'), (b'THU', b'Thursday'), (b'FRI', b'Friday'), (b'SAT', b'Saturday')], default=b'MON', max_length=3)),
                ('starttime', models.TimeField()),
                ('endtime', models.TimeField()),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intelligent_scheduler.Faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('roomid', models.IntegerField(primary_key=True, serialize=False)),
                ('max_strength', models.IntegerField(default=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('rollnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('batch', models.CharField(choices=[(b'UG1', b'UG1'), (b'UG2', b'UG2'), (b'UG3', b'UG3'), (b'UG4', b'UG4')], default=b'UG1', max_length=4)),
                ('branch', models.CharField(choices=[(b'CSE', b'CSE'), (b'ECE', b'ECE')], default=b'CSE', max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='TeachingAssistant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intelligent_scheduler.Courses')),
                ('rollnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intelligent_scheduler.Student')),
            ],
        ),
        migrations.AddField(
            model_name='coursetaken',
            name='rollnumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intelligent_scheduler.Student'),
        ),
        migrations.AddField(
            model_name='courses',
            name='fid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intelligent_scheduler.Faculty'),
        ),
    ]
