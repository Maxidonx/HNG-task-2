# Generated by Django 4.2.5 on 2023-09-13 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peopleAPI', '0007_alter_person_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
