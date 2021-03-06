# Generated by Django 2.2.3 on 2020-03-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='phone2',
            field=models.CharField(max_length=20, null=True, verbose_name='联系电话2'),
        ),
        migrations.AlterField(
            model_name='stud',
            name='primarySchool',
            field=models.CharField(max_length=50, null=True, verbose_name='毕业小学'),
        ),
        migrations.AlterField(
            model_name='stud',
            name='specialty',
            field=models.CharField(max_length=200, null=True, verbose_name='特长'),
        ),
        migrations.AlterField(
            model_name='stud',
            name='testRank1',
            field=models.IntegerField(null=True, verbose_name='初三上学期期中考年级排名'),
        ),
        migrations.AlterField(
            model_name='stud',
            name='testRank2',
            field=models.IntegerField(null=True, verbose_name='初三上学期期末考年级排名'),
        ),
        migrations.AlterField(
            model_name='stud',
            name='testScore1',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='初三上学期期中考成绩'),
        ),
        migrations.AlterField(
            model_name='stud',
            name='testScore2',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='初三上学期期末考成绩'),
        ),
    ]
