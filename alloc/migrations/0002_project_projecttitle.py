# Generated by Django 2.2.4 on 2019-08-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alloc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projecttitle',
            field=models.CharField(max_length=250, null=True),
        ),
    ]