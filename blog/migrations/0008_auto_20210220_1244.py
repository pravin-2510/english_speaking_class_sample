# Generated by Django 3.1.6 on 2021-02-20 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210220_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='admin', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
