# Generated by Django 3.0.9 on 2020-09-10 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_locking'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='draftversion',
            options={
                'get_latest_by': 'created',
                'permissions': (('owner', 'Owns the draft dandiset'),),
            },
        ),
    ]