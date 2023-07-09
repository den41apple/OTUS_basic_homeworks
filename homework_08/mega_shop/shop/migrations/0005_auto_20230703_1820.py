# Generated by Django 4.2.2 on 2023-07-03 15:20

from django.db import migrations

CATEGORY_NAME = "default"

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Category = apps.get_model("shop", "Category")
    Product = apps.get_model("shop", "Product")
    db_alias = schema_editor.connection.alias
    default_category, created = Category.objects.using(db_alias).get_or_create(
        name=CATEGORY_NAME, description="default category"
    )
    Product.objects.update(category=default_category)


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    Category = apps.get_model("shop", "Category")
    db_alias = schema_editor.connection.alias
    Product = apps.get_model("shop", "Product")
    Product.objects.update(category=None)

class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0004_product_category"),
    ]

    operations = [
        migrations.RunPython(code=forwards_func, reverse_code=reverse_func)
    ]
