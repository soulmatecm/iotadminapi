# Generated by Django 2.1.5 on 2019-01-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='姓名'),
        ),
    ]
