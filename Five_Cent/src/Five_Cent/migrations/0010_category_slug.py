# Generated by Django 3.1.7 on 2021-03-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Five_Cent', '0009_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
