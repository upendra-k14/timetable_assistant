from django.db.models import *
from intelligent_scheduler.config import model_choices

class Courses(Model):
    cid = CharField(max_length=10, primary_key=True)
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
    fid = IntegerField()
    preferred_day = CharField(
        max_length=3,
        choices=model_choices['WEEK_DAY'],
        default='MON')
    starttime = TimeField()
    endtime = TimeField()

class Rooms(Model):
    roomid = IntegerField()
    max_strength = IntegerField(default=50)

class Student(Model):
    rollnumber = IntegerField()
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1')
    branch = CharField(
        max_length=4,
        choices=model_choices['BRANCH'],
        default='CSE')

class CourseTaken(Model):
    rollnumber = IntegerField()
    cid = CharField(max_length=10)

class TeachingAssistant(Model):
    rollnumber = IntegerField()
    cid = CharField(max_length=10)

class ClassDuration(Model):
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1')
    duration = DurationField()

class CourseType(Model):
    cid = CharField(max_length=10)
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
        default='UG1')
    starttime = TimeField()
    endtime = TimeField()
