# Generated by Django 3.1.7 on 2021-03-03 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Five_Cent', '0007_auto_20210303_0247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Product Image', 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]