# Generated by Django 5.0 on 2024-02-17 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_app', '0013_teacher_remove_user_role_course_teachers_delete_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teachers',
            new_name='teacher',
        ),
    ]
