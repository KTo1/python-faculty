# Generated by Django 3.2.6 on 2022-05-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_userprofile_langs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='langs',
            field=models.TextField(blank=True, verbose_name='языки'),
        ),
    ]
