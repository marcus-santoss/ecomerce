# Generated by Django 5.1 on 2024-08-28 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_product_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(default="AVAILABLE", max_length=11),
        ),
    ]
