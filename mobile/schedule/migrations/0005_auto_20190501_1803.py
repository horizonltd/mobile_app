# Generated by Django 2.1.7 on 2019-05-02 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0004_remove_speaker_conference_paper'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='entry_id',
            new_name='membership_Registration_Number',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='membership_id',
        ),
    ]
