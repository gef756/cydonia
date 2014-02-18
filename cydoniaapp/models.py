from django.db import models

# Create your models here.
class User(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email_address = models.EmailField(blank=True, unique=True)
    username = models.CharField(max_length=30, unique=True)
    badges = models.ManyToManyField('Badge')

class Student (User):
    teacher = models.ManyToManyField('Teacher')
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)

class Teacher (User):
    curriculum_group = models.ForeignKey('CurriculumGroup')

class GradeBook (models.Model):
    assignment = models.ForeignKey('Assignment')
    student = models.ForeignKey('Student')
    question = models.ForeignKey('Question')
    grade = models.DecimalField(max_digits=5, decimal_places=2)

class AttendanceBook (models.Model): 
    student = models.ForeignKey('Student')
    date = models.DateField()
    attendance = models.DecimalField(max_digits=3, decimal_places=2)

class Curriculum (models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey('CurriculumGroup')

class CurriculumGroup (models.Model):
    name = models.CharField(max_length=50)

class CurriculumRequirement (models.Model):
    curriculum = models.ManyToManyField('Curriculum')

class Assignment (models.Model):
    HOMEWORK = 'HW'    
    TEST = 'TS'
    QUIZ = 'QZ'
    ASSIGNMENT_TYPES = (
        (HOMEWORK, 'Homework'),
        (QUIZ, 'Quiz'),
        (TEST, 'Test'),
    )
    curriculum_requirement = models.ManyToManyField('CurriculumRequirement')
    assignment_type = models.CharField(max_length=2,
                                       choices=ASSIGNMENT_TYPES,
                                       default=HOMEWORK)
    due_date = models.DateField(blank=True)
    start_date = models.DateField(blank=True)
     

class Question (models.Model):
    assignment = models.ManyToManyField('Assignment')

class SchoolClass (models.Model):
    curriculum = models.ForeignKey('Curriculum')
    grade_book = models.OneToOneField('GradeBook')
    attendance_book = models.OneToOneField('AttendanceBook')
    teacher = models.ForeignKey('Teacher')

class Goal (models.Model):
    owner = models.ForeignKey('User')
    target = models.ForeignKey('Student', related_name='student_target') 
    description = models.CharField(max_length=255)

class Badge (models.Model):
    name = models.CharField(max_length=30)

class Levels (models.Model):
    level_no = models.IntegerField()
    minimum_xp = models.IntegerField()

