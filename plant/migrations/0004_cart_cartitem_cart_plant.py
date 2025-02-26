# Generated by Django 5.1.4 on 2025-02-26 07:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0003_blog'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cart_items', to='plant.cart')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plant.plant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='plant',
            field=models.ManyToManyField(through='plant.CartItem', to='plant.plant'),
        ),
    ]
