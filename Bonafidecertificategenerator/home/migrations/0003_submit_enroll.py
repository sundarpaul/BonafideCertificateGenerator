# Generated by Django 3.1.4 on 2021-01-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210123_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='submit',
            name='enroll',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
