# Generated by Django 3.1.7 on 2021-04-17 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arxiv', '0003_auto_20210418_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paperinfo',
            name='pdf_url',
            field=models.CharField(max_length=50),
        ),
    ]
