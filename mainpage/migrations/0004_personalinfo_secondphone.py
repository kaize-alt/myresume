# Generated by Django 5.1.2 on 2024-12-28 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_personalinfo_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='secondphone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
