# Generated by Django 2.1.7 on 2019-02-18 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_sec', models.CharField(max_length=50)),
                ('days', models.IntegerField(choices=[(1, 'M'), (2, 'T'), (3, 'W'), (4, 'Th'), (5, 'F'), (6, 'St'), (7, 'Sn')])),
                ('slots', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14')])),
                ('course_name', models.CharField(max_length=100)),
                ('instr', models.CharField(max_length=100)),
                ('quota', models.IntegerField(default=0)),
                ('dep', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Courses.Department')),
            ],
        ),
    ]