# Generated by Django 4.2.6 on 2023-11-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='products/noimg.png', upload_to='products/%Y/%m/%d'),
        ),
    ]
