# Generated by Django 4.2.1 on 2023-05-30 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company_contacts',
            new_name='Company_contact',
        ),
        migrations.RenameModel(
            old_name='Images',
            new_name='Image',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
