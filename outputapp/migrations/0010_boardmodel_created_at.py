# Generated by Django 3.0.4 on 2020-04-04 22:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('outputapp', '0009_auto_20200404_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
    ]
