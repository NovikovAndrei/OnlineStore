# Generated by Django 4.2.1 on 2023-06-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/category'),
        ),
    ]
