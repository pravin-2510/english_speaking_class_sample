# Generated by Django 3.1.6 on 2021-02-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_contact_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]