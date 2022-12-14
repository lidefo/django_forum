# Generated by Django 4.1.1 on 2022-10-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_alter_topic_description_alter_topic_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(max_length=3500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]
