# Generated by Django 2.2.5 on 2019-10-04 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191004_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='itemsize',
            field=models.CharField(choices=[('s', 'Small'), ('l', 'Lagre')], default='s', max_length=1),
        ),
        migrations.AlterField(
            model_name='orders',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Items'),
        ),
    ]