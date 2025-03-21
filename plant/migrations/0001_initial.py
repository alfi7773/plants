# Generated by Django 5.1.4 on 2025-02-21 20:07

import django.db.models.deletion
import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('living_room', models.TextField()),
                ('dinig_room', models.TextField()),
                ('ofice', models.TextField()),
            ],
            options={
                'verbose_name': 'description',
                'verbose_name_plural': 'descriptions',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('small', 'small'), ('medium', 'medium'), ('large', 'large')], default='small', max_length=50)),
            ],
            options={
                'verbose_name': 'size',
                'verbose_name_plural': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('short_description', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='plant', to='plant.category')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plant.description')),
                ('sizes', models.ManyToManyField(related_name='plant', to='plant.size')),
                ('tags', models.ManyToManyField(related_name='plant', to='plant.tag')),
            ],
            options={
                'verbose_name': 'plant',
                'verbose_name_plural': 'plants',
            },
        ),
        migrations.CreateModel(
            name='ImagePlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=90, scale=None, size=[1920, 1080], upload_to='plant_images/')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='plant.plant')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]
