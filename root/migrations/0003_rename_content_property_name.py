# Generated by Django 4.2 on 2024-08-08 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_property_question_s_service_skills_trainer_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='content',
            new_name='name',
        ),
    ]