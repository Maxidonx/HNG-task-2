# Generated by Django 4.2.5 on 2023-09-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleAPI', '0006_rename_interns_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='fullname',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]