# Generated by Django 2.0.7 on 2019-01-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190106_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='degree',
            field=models.CharField(blank=True, help_text='Enter a degree of the tutor', max_length=30, null=True),
        ),
    ]
