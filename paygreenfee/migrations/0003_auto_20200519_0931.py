# Generated by Django 3.0.6 on 2020-05-19 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paygreenfee', '0002_auto_20200519_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentinfo',
            old_name='total_price',
            new_name='total_greenfee',
        ),
    ]
