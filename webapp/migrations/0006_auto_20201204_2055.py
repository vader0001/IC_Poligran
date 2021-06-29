# Generated by Django 3.1.3 on 2020-12-05 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20201203_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='room_number',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='', upload_to='webapp/static/images'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('delivered', 'Entregada'), ('preparing', 'En preparación')], default='preparing', max_length=10),
        ),
    ]
