# Generated by Django 3.2 on 2021-06-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solucion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nota',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]