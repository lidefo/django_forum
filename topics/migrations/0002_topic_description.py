# Generated by Django 4.1.1 on 2022-10-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='description',
            field=models.CharField(default=0, max_length=3500, verbose_name='Описание'),
            preserve_default=False,
        ),
    ]
