from django.db.models import *
from intelligent_scheduler.config import model_choices

class Courses(Model):
    cid = CharField(max_length=10, primary_key=True)
    fid = ForeignKey(
        'Faculty',
        on_delete=CASCADE)
    cname = CharField(max_length=100, unique=True)
    cshortname = CharField(max_length=6, unique=True)
    nclasses = IntegerField(default=2)
    ntutorials = IntegerField(default=2)
    expectedstrength = IntegerField(default=50)

    def __str__(self):
        return '{} {} [{}]'.format(self.cid,self.cname,self.cshortname)

class Faculty(Model):
    fname = CharField(max_length=100)
    fshortname = CharField(max_length=4, unique=True)
    isvisiting = BooleanField(default=False)

    def __str__(self):
        return '{} [{}]'.format(self.fname,self.fshortname)

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

    def __str__(self):
        return '{} {}'.format(str(self.fid),str(self.preferred_day))

class Rooms(Model):
    roomid = IntegerField(primary_key=True)
    max_strength = IntegerField(default=50)

    def __str__(self):
        return '{} {}'.format(str(self.roomid),self.max_strength)

class Student(Model):
    rollnumber = CharField(max_length=12, primary_key=True)
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1')
    branch = CharField(
        max_length=4,
        choices=model_choices['BRANCH'],
        default='CSE')

    def __str__(self):
        return str(self.rollnumber)

class CourseTaken(Model):
    rollnumber = ForeignKey(
        'Student',
        on_delete=CASCADE)
    cid = ForeignKey(
        'Courses',
        on_delete=CASCADE)

    class Meta:
        unique_together = ('rollnumber','cid')

    def __str__(self):
        return '{} {}'.format(str(self.rollnumber),str(self.cid))

class TeachingAssistant(Model):
    rollnumber = ForeignKey(
        'Student',
        on_delete=CASCADE)
    cid = ForeignKey(
        'Courses',
        on_delete=CASCADE)

    class Meta:
        unique_together = ('rollnumber','cid')

    def __str__(self):
        return '{} {}'.format(str(self.rollnumber),str(self.cid))

class ClassDuration(Model):
    batch = CharField(
        primary_key=True,
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1')
    duration = DurationField()

    def __str__(self):
        return '{} {}'.format(str(self.batch),str(self.duration))

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

    class Meta:
        unique_together = ('cid','batch','branch')

    def __str__(self):
        return '{} {} {}'.format(str(self.cid),str(self.batch),str(self.branch))

class LunchBreak(Model):
    batch = CharField(
        max_length=4,
        choices=model_choices['BATCH'],
        default='UG1',
        primary_key=True)
    starttime = TimeField()
    endtime = TimeField()

    def __str__(self):
        return str(self.batch)
