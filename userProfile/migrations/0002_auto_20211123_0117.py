# Generated by Django 3.2.8 on 2021-11-23 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='date_of_birth',
            new_name='dateOfBirth',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='display_picture',
            new_name='displayPicture',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='education_level',
            new_name='educationLevel',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='n_i_n',
            new_name='ninNumber',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
    ]
