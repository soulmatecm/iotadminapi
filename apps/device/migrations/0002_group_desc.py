# Generated by Django 2.1.5 on 2019-01-27 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='desc',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='分组描述'),
        ),
    ]
