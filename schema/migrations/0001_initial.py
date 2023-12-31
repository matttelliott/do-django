# Generated by Django 4.2.6 on 2023-10-29 20:02

from django.db import migrations, models
import django.db.models.deletion
import functools
import schema.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email_address', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=functools.partial(schema.models.image_path, *('author',), **{}))),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=functools.partial(schema.models.image_path, *('article',), **{}))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='schema.author')),
            ],
        ),
    ]
