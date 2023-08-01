# Generated by Django 4.2.2 on 2023-07-05 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0007_alter_category_options_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Archived"), (1, "Availible")], default=1
            ),
            preserve_default=False,
        ),
    ]