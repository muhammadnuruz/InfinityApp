# Generated by Django 5.0.1 on 2024-05-14 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='group_id',
            field=models.CharField(default='salom', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]