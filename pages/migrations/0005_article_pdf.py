# Generated by Django 5.0.2 on 2024-02-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_userquizstats'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pdf',
            field=models.FileField(blank=True, upload_to='article_pdfs/'),
        ),
    ]
