# Generated by Django 3.2.6 on 2022-06-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20220410_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='basic_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]