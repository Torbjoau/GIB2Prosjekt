<<<<<<< HEAD
# Generated by Django 3.2.12 on 2022-04-21 09:58
=======
# Generated by Django 4.0.3 on 2022-04-19 10:38
>>>>>>> kart

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bolig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.DecimalField(decimal_places=1, max_digits=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='address')),
<<<<<<< HEAD
                ('image', models.ImageField(blank=True, upload_to='media')),
                ('type', models.CharField(default='Enebolig', max_length=20)),
                ('bedroom', models.IntegerField(default=2)),
                ('energy', models.CharField(default='A', max_length=1)),
                ('area', models.IntegerField(default=155)),
                ('year', models.IntegerField(default=2012)),
=======
>>>>>>> kart
            ],
        ),
    ]
