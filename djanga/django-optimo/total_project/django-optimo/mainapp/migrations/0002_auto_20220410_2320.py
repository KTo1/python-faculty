# Generated by Django 3.2.6 on 2022-04-10 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategories',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this category should be treated as active. '),
        ),
        migrations.AddField(
            model_name='products',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this product should be treated as active. '),
        ),
    ]