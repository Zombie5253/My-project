# Generated by Django 2.0 on 2020-12-14 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201206_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='average_Rating',
            field=models.FloatField(),
        ),
    ]
