# Generated by Django 3.1.1 on 2020-11-22 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0024_auto_20201122_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='backend.restaurant'),
        ),
    ]
