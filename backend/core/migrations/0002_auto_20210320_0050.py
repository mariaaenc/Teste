# Generated by Django 3.1.7 on 2021-03-20 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='stacks',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]