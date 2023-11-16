# Generated by Django 4.2.6 on 2023-11-16 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_category_unique_together'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='category',
            name='shop_catego_name_289c7e_idx',
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'main_category')},
        ),
    ]