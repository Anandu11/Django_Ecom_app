# Generated by Django 3.1.5 on 2024-01-30 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='data_order',
            new_name='date_order',
        ),
    ]
