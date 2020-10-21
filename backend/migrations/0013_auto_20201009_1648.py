# Generated by Django 3.1.1 on 2020-10-09 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_review_is_useful'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['headline'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='restaurant',
            options={'ordering': ['name'], 'verbose_name': 'Рестаран', 'verbose_name_plural': 'Рестораны'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['headline'], 'verbose_name': 'Обзор', 'verbose_name_plural': 'Обзоры'},
        ),
    ]