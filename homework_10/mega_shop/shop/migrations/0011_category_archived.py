# Generated by Django 4.2.3 on 2023-07-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0010_product_expiration_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]
