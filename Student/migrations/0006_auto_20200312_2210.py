# Generated by Django 2.2.3 on 2020-03-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_auto_20200312_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='specialty',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='特长'),
        ),
    ]