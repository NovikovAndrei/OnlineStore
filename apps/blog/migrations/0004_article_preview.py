# Generated by Django 4.2.1 on 2023-07-08 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
