# Generated by Django 3.1.5 on 2024-02-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20240131_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
