# Generated by Django 4.2.7 on 2024-09-27 10:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapps', '0003_remove_template_file_path_template_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='brief',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
