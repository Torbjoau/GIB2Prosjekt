# Generated by Django 4.0.3 on 2022-04-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gib2Prosjekt', '0005_alter_bolig_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bolig',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/media'),
        ),
    ]
