# Generated by Django 4.2.4 on 2023-08-16 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fridge_app', '0004_alter_receipt_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='item_list',
            field=models.TextField(default='first item', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='', verbose_name='Image'),
            preserve_default=False,
        ),
    ]