from django.db.models import *
from intelligent_scheduler.config import model_choices

class Courses(Model):
    cid = CharField(max_length=10, primary_key=True)
    fid = ForeignKey(
        'Faculty',
        on_delete=CASCADE)
    cname = CharField(max_length=100)
    cshortname = CharField(max_length=6)
    nclasses = IntegerField(default=2)
    ntutorials = IntegerField(default=2)
    expectedstrength = IntegerField(default=50)

class Faculty(Model):
    fname = CharField(max_length=100)
    fshortname = CharField(max_length=4)
    isvisiting = BooleanField(default=False)

class PreferredFacultyHours(Model):
    fid = ForeignKey(
        'Faculty',
        on_delete=CASCADE)
    preferred_day = CharField(
        max_length=3,
        choices=model_choices['WEEK_DAY'],
        default='MON')
    starttime = TimeField()
    endtime = TimeField()

class Rooms(Model):
    roomid = IntegerField(primary_key=True)
    max_strength = IntegerField(default=50)

class Student(Model):
    rollnumber = IntegerField(primary_key=True)
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1')
    branch = CharField(
        max_length=4,
        choices=model_choices['BRANCH'],
        default='CSE')

class CourseTaken(Model):
    rollnumber = ForeignKey(
        'Student',
        on_delete=CASCADE)
    cid = ForeignKey(
        'Courses',
        on_delete=CASCADE)

class TeachingAssistant(Model):
    rollnumber = ForeignKey(
        'Student',
        on_delete=CASCADE)
    cid = ForeignKey(
        'Courses',
        on_delete=CASCADE)

class ClassDuration(Model):
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1')
    duration = DurationField()

class CourseType(Model):
    cid = ForeignKey(
        'Courses',
        on_delete=CASCADE)
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1')
    branch = CharField(
        max_length=4,
        choices=model_choices['BRANCH'],
        default='CSE')
    course_type = CharField(
        max_length=4,
        choices=model_choices['COURSE_TYPE'])

class LunchBreak(Model):
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1',
        primary_key=True)
    starttime = TimeField()
    endtime = TimeField()
