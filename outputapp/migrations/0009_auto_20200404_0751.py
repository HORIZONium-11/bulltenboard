# Generated by Django 3.0.4 on 2020-04-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outputapp', '0008_auto_20200401_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]