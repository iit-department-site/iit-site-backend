# Generated by Django 3.2.5 on 2022-10-16 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_usernet_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]