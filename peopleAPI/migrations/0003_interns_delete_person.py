# Generated by Django 4.2.5 on 2023-09-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleAPI', '0002_alter_person_first_name_alter_person_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('track', models.CharField(max_length=50)),
                ('stage', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]