# Generated by Django 4.1.4 on 2023-02-07 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_article_image_alter_article_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='article_images/'),
        ),
    ]
