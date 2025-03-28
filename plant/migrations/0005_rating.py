# Generated by Django 5.1.4 on 2025-03-02 16:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0004_cart_cartitem_cart_plant'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('score', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='plant.plant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'rating',
                'verbose_name_plural': 'ratings',
            },
        ),
    ]
