# Generated by Django 3.1.3 on 2020-12-05 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20201204_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='Item',
            new_name='item',
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('order', 'item')},
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='customer',
        ),
    ]
