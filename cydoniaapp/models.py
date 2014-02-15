from django.db import models

# Create your models here.
class User(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)

class Student (User):
    teacher = models.ManyToManyField('Teacher')

class Teacher (User):
    curriculum_group = models.ForeignKey('CurriculumGroup')

class GradeBook (models.Model):
    assignment = models.ForeignKey('Assignment')
    student = models.ForeignKey('Student')
    question = models.ForeignKey('Question')
    grade = models.DecimalField(max_digits=4, decimal_places=2)

class Curriculum (models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey('CurriculumGroup')

class CurriculumGroup (models.Model):
    name = models.CharField(max_length=50)

class CurriculumRequirement (models.Model):
    curriculum = models.ManyToManyField('Curriculum')

class Assignment (models.Model):
    curriculum_requirement = models.ManyToManyField('CurriculumRequirement')

class Question (models.Model):
    assignment = models.ManyToManyField('Question')

class SchoolClass (models.Model):
    curriculum = models.ForeignKey('Curriculum')
    grade_book = models.OneToOneField('GradeBook')
    teacher = models.ForeignKey('Teacher')

class Goal (models.Model):
    owner = models.ForeignKey('User')
    target = models.ForeignKey('Student', related_name='student_target') 
    description = models.CharField(max_length=255)
