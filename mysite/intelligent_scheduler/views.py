from django.shortcuts import render
from django.db import connection
from collections import namedtuple


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"

    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def get_courses(batch, branch=None):
    """
    Should return:
    courseid
    facultyid
    coursename,
    courseshortname,
    facultyname,
    facultyshortname,
    """

    table_prefix = 'intelligent_scheduler_'
    course_table = '{}courses'.format(table_prefix)
    faculty_table = '{}faculty'.format(table_prefix)
    ctype_table = '{}coursetype'.format(table_prefix)
    rows = None

    if branch:
        with connection.cursor() as cursor:
            cursor.execute("select distinct(cid) as courseid, \
                           fid_id as facultyid, \
                           cname as coursename,\
                           cshortname as coursehortname,\
                           fname as facultyname,\
                           fshortname as facultyshortname from\
                           ({} join {} on cid=cid_id) join {} on fid_id={}.id\
                            where batch=%s and branch=%s".format(
                                course_table,
                                ctype_table,
                                faculty_table,
                                faculty_table), [batch, branch])
            rows = namedtuplefetchall(cursor)

    else:
        with connection.cursor() as cursor:
            cursor.execute("select distinct(cid) as courseid, \
                           fid_id as facultyid, \
                           cname as coursename,\
                           cshortname as coursehortname,\
                           fname as facultyname,\
                           fshortname as facultyshortname from\
                           ({} join {} on cid=cid_id) join {} on fid_id={}.id\
                            where batch=%s".format(
                                course_table,
                                ctype_table,
                                faculty_table,
                                faculty_table), [batch])
            rows = namedtuplefetchall(cursor)
    return rows


def fullcalendar(request):
    return render(request, 'intelligent_scheduler/fullweekcalendar.html')


def index(request):
    ug4_cse_courses = get_courses('UG4', 'CSE')
    ug4_ece_courses = get_courses('UG4', 'ECE')
    ug3_cse_courses = get_courses('UG3', 'CSE')
    ug3_ece_courses = get_courses('UG3', 'ECE')
    ug2_courses = get_courses('UG2')
    ug1_courses = get_courses('UG1')
    # print(ug4_cse_courses[0].coursename)
    return render(
        request,
        'intelligent_scheduler/index.html',
        {
            'ug4_cse_courses': ug4_cse_courses,
            'ug4_ece_courses': ug4_ece_courses,
            'ug3_cse_courses': ug3_cse_courses,
            'ug3_ece_courses': ug3_ece_courses,
            'ug2_courses': ug2_courses,
            'ug1_courses': ug1_courses,
        })
