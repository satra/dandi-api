# Generated by Django 3.0.9 on 2020-08-28 20:13

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0009_rename_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True, verbose_name='created'
            ),
        ),
        migrations.AlterField(
            model_name='asset',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, verbose_name='modified'
            ),
        ),
        migrations.AlterField(
            model_name='dandiset',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True, verbose_name='created'
            ),
        ),
        migrations.AlterField(
            model_name='dandiset',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, verbose_name='modified'
            ),
        ),
        migrations.AlterField(
            model_name='draftversion',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True, verbose_name='created'
            ),
        ),
        migrations.AlterField(
            model_name='draftversion',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, verbose_name='modified'
            ),
        ),
        migrations.AlterField(
            model_name='version',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True, verbose_name='created'
            ),
        ),
        migrations.AlterField(
            model_name='version',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True, verbose_name='modified'
            ),
        ),
    ]
