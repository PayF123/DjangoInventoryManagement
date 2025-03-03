# Generated by Django 5.1.2 on 2024-12-18 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_product_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='identity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='make',
        ),
        migrations.RemoveField(
            model_name='product',
            name='package_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specification',
        ),
        migrations.RemoveField(
            model_name='product',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tol_percentage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='uom',
        ),
        migrations.CreateModel(
            name='Assembly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('specification', models.CharField(max_length=255)),
                ('supplier', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('package_size', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('uom', models.CharField(max_length=50)),
                ('identity', models.CharField(max_length=50)),
                ('tol_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('assembly', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.assembly')),
            ],
        ),
    ]
