# Generated by Django 4.2.6 on 2023-11-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products/noimg.png', upload_to='products/%Y/%m/%d'),
        ),
    ]
