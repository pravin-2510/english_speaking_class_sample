# Generated by Django 3.1.6 on 2021-02-20 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210220_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contact_date',
            new_name='Created_date',
        ),
    ]
