# Generated by Django 3.2.7 on 2021-09-11 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pinkingweb', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Task_models',
        ),
        migrations.RenameModel(
            old_name='Testcase',
            new_name='Testcase_models',
        ),
    ]