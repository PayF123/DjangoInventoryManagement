# Generated by Django 5.1.2 on 2024-12-18 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_assembly_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='assembly',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='components', to='dashboard.assembly'),
        ),
    ]
