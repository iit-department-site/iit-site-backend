# Generated by Django 3.2.5 on 2022-12-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_auto_20221204_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernet',
            name='first_login',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]