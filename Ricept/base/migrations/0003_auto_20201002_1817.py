# Generated by Django 3.0.3 on 2020-10-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201002_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]
