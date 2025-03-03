# Generated by Django 5.1.2 on 2024-12-13 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_product_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='identity',
            field=models.CharField(default='RS1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='make',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='package_size',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='tol_percentage',
            field=models.DecimalField(decimal_places=2, default=0.01, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='uom',
            field=models.CharField(default='N/A', max_length=50),
            preserve_default=False,
        ),
    ]
