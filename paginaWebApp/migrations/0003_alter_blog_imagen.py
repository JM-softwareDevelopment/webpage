# Generated by Django 4.2.4 on 2023-09-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginaWebApp', '0002_rename_subtitulo_blog_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
