# Generated by Django 3.0.4 on 2020-04-01 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outputapp', '0006_auto_20200401_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='category',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='url_code',
            field=models.CharField(default='aaa', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]