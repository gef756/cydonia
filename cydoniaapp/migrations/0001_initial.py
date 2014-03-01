# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'cydoniaapp_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email_address', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'cydoniaapp', ['User'])

        # Adding M2M table for field badges on 'User'
        db.create_table(u'cydoniaapp_user_badges', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'cydoniaapp.user'], null=False)),
            ('badge', models.ForeignKey(orm[u'cydoniaapp.badge'], null=False))
        ))
        db.create_unique(u'cydoniaapp_user_badges', ['user_id', 'badge_id'])

        # Adding model 'Student'
        db.create_table(u'cydoniaapp_student', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cydoniaapp.User'], unique=True, primary_key=True)),
            ('points', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'cydoniaapp', ['Student'])

        # Adding M2M table for field teacher on 'Student'
        db.create_table(u'cydoniaapp_student_teacher', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('student', models.ForeignKey(orm[u'cydoniaapp.student'], null=False)),
            ('teacher', models.ForeignKey(orm[u'cydoniaapp.teacher'], null=False))
        ))
        db.create_unique(u'cydoniaapp_student_teacher', ['student_id', 'teacher_id'])

        # Adding model 'Teacher'
        db.create_table(u'cydoniaapp_teacher', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cydoniaapp.User'], unique=True, primary_key=True)),
            ('curriculum_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.CurriculumGroup'])),
        ))
        db.send_create_signal(u'cydoniaapp', ['Teacher'])

        # Adding model 'GradeBook'
        db.create_table(u'cydoniaapp_gradebook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assignment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.Assignment'])),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.Student'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.Question'])),
            ('grade', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'cydoniaapp', ['GradeBook'])

        # Adding model 'AttendanceBook'
        db.create_table(u'cydoniaapp_attendancebook', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.Student'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('attendance', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
        ))
        db.send_create_signal(u'cydoniaapp', ['AttendanceBook'])

        # Adding model 'Curriculum'
        db.create_table(u'cydoniaapp_curriculum', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.CurriculumGroup'])),
        ))
        db.send_create_signal(u'cydoniaapp', ['Curriculum'])

        # Adding model 'CurriculumGroup'
        db.create_table(u'cydoniaapp_curriculumgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'cydoniaapp', ['CurriculumGroup'])

        # Adding model 'CurriculumRequirement'
        db.create_table(u'cydoniaapp_curriculumrequirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cydoniaapp', ['CurriculumRequirement'])

        # Adding M2M table for field curriculum on 'CurriculumRequirement'
        db.create_table(u'cydoniaapp_curriculumrequirement_curriculum', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('curriculumrequirement', models.ForeignKey(orm[u'cydoniaapp.curriculumrequirement'], null=False)),
            ('curriculum', models.ForeignKey(orm[u'cydoniaapp.curriculum'], null=False))
        ))
        db.create_unique(u'cydoniaapp_curriculumrequirement_curriculum', ['curriculumrequirement_id', 'curriculum_id'])

        # Adding model 'Assignment'
        db.create_table(u'cydoniaapp_assignment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('assignment_type', self.gf('django.db.models.fields.CharField')(default='HW', max_length=2)),
            ('due_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'cydoniaapp', ['Assignment'])

        # Adding M2M table for field curriculum_requirement on 'Assignment'
        db.create_table(u'cydoniaapp_assignment_curriculum_requirement', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('assignment', models.ForeignKey(orm[u'cydoniaapp.assignment'], null=False)),
            ('curriculumrequirement', models.ForeignKey(orm[u'cydoniaapp.curriculumrequirement'], null=False))
        ))
        db.create_unique(u'cydoniaapp_assignment_curriculum_requirement', ['assignment_id', 'curriculumrequirement_id'])

        # Adding model 'Question'
        db.create_table(u'cydoniaapp_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'cydoniaapp', ['Question'])

        # Adding M2M table for field assignment on 'Question'
        db.create_table(u'cydoniaapp_question_assignment', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('question', models.ForeignKey(orm[u'cydoniaapp.question'], null=False)),
            ('assignment', models.ForeignKey(orm[u'cydoniaapp.assignment'], null=False))
        ))
        db.create_unique(u'cydoniaapp_question_assignment', ['question_id', 'assignment_id'])

        # Adding model 'SchoolClass'
        db.create_table(u'cydoniaapp_schoolclass', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('curriculum', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.Curriculum'])),
            ('grade_book', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cydoniaapp.GradeBook'], unique=True)),
            ('attendance_book', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cydoniaapp.AttendanceBook'], unique=True)),
            ('teacher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.Teacher'])),
        ))
        db.send_create_signal(u'cydoniaapp', ['SchoolClass'])

        # Adding model 'Goal'
        db.create_table(u'cydoniaapp_goal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cydoniaapp.User'])),
            ('target', self.gf('django.db.models.fields.related.ForeignKey')(related_name='student_target', to=orm['cydoniaapp.Student'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'cydoniaapp', ['Goal'])

        # Adding model 'Badge'
        db.create_table(u'cydoniaapp_badge', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'cydoniaapp', ['Badge'])

        # Adding model 'Levels'
        db.create_table(u'cydoniaapp_levels', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('level_no', self.gf('django.db.models.fields.IntegerField')()),
            ('minimum_xp', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'cydoniaapp', ['Levels'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'cydoniaapp_user')

        # Removing M2M table for field badges on 'User'
        db.delete_table('cydoniaapp_user_badges')

        # Deleting model 'Student'
        db.delete_table(u'cydoniaapp_student')

        # Removing M2M table for field teacher on 'Student'
        db.delete_table('cydoniaapp_student_teacher')

        # Deleting model 'Teacher'
        db.delete_table(u'cydoniaapp_teacher')

        # Deleting model 'GradeBook'
        db.delete_table(u'cydoniaapp_gradebook')

        # Deleting model 'AttendanceBook'
        db.delete_table(u'cydoniaapp_attendancebook')

        # Deleting model 'Curriculum'
        db.delete_table(u'cydoniaapp_curriculum')

        # Deleting model 'CurriculumGroup'
        db.delete_table(u'cydoniaapp_curriculumgroup')

        # Deleting model 'CurriculumRequirement'
        db.delete_table(u'cydoniaapp_curriculumrequirement')

        # Removing M2M table for field curriculum on 'CurriculumRequirement'
        db.delete_table('cydoniaapp_curriculumrequirement_curriculum')

        # Deleting model 'Assignment'
        db.delete_table(u'cydoniaapp_assignment')

        # Removing M2M table for field curriculum_requirement on 'Assignment'
        db.delete_table('cydoniaapp_assignment_curriculum_requirement')

        # Deleting model 'Question'
        db.delete_table(u'cydoniaapp_question')

        # Removing M2M table for field assignment on 'Question'
        db.delete_table('cydoniaapp_question_assignment')

        # Deleting model 'SchoolClass'
        db.delete_table(u'cydoniaapp_schoolclass')

        # Deleting model 'Goal'
        db.delete_table(u'cydoniaapp_goal')

        # Deleting model 'Badge'
        db.delete_table(u'cydoniaapp_badge')

        # Deleting model 'Levels'
        db.delete_table(u'cydoniaapp_levels')


    models = {
        u'cydoniaapp.assignment': {
            'Meta': {'object_name': 'Assignment'},
            'assignment_type': ('django.db.models.fields.CharField', [], {'default': "'HW'", 'max_length': '2'}),
            'curriculum_requirement': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cydoniaapp.CurriculumRequirement']", 'symmetrical': 'False'}),
            'due_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        u'cydoniaapp.attendancebook': {
            'Meta': {'object_name': 'AttendanceBook'},
            'attendance': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.Student']"})
        },
        u'cydoniaapp.badge': {
            'Meta': {'object_name': 'Badge'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'cydoniaapp.curriculum': {
            'Meta': {'object_name': 'Curriculum'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.CurriculumGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'cydoniaapp.curriculumgroup': {
            'Meta': {'object_name': 'CurriculumGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'cydoniaapp.curriculumrequirement': {
            'Meta': {'object_name': 'CurriculumRequirement'},
            'curriculum': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cydoniaapp.Curriculum']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cydoniaapp.goal': {
            'Meta': {'object_name': 'Goal'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.User']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'student_target'", 'to': u"orm['cydoniaapp.Student']"})
        },
        u'cydoniaapp.gradebook': {
            'Meta': {'object_name': 'GradeBook'},
            'assignment': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.Assignment']"}),
            'grade': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.Question']"}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.Student']"})
        },
        u'cydoniaapp.levels': {
            'Meta': {'object_name': 'Levels'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_no': ('django.db.models.fields.IntegerField', [], {}),
            'minimum_xp': ('django.db.models.fields.IntegerField', [], {})
        },
        u'cydoniaapp.question': {
            'Meta': {'object_name': 'Question'},
            'assignment': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cydoniaapp.Assignment']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'cydoniaapp.schoolclass': {
            'Meta': {'object_name': 'SchoolClass'},
            'attendance_book': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cydoniaapp.AttendanceBook']", 'unique': 'True'}),
            'curriculum': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.Curriculum']"}),
            'grade_book': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cydoniaapp.GradeBook']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teacher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.Teacher']"})
        },
        u'cydoniaapp.student': {
            'Meta': {'object_name': 'Student', '_ormbases': [u'cydoniaapp.User']},
            'level': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'teacher': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cydoniaapp.Teacher']", 'symmetrical': 'False'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cydoniaapp.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cydoniaapp.teacher': {
            'Meta': {'object_name': 'Teacher', '_ormbases': [u'cydoniaapp.User']},
            'curriculum_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cydoniaapp.CurriculumGroup']"}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cydoniaapp.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cydoniaapp.user': {
            'Meta': {'object_name': 'User'},
            'badges': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cydoniaapp.Badge']", 'symmetrical': 'False'}),
            'email_address': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['cydoniaapp']