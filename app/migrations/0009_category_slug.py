# Generated by Django 4.1.7 on 2023-03-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_customer_phone_seller_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='something'),
            preserve_default=False,
        ),
    ]
