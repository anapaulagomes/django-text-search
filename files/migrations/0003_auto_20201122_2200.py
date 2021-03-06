# Generated by Django 3.1.2 on 2020-11-22 21:00

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20201030_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='content_search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AddIndex(
            model_name='file',
            index=django.contrib.postgres.indexes.GinIndex(fields=['content_search_vector'], name='files_file_content_e90501_gin'),
        ),
    ]
