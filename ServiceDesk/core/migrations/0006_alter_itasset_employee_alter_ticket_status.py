# Generated by Django 5.0.2 on 2024-08-07 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_assigned_by_itasset_assigned_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itasset',
            name='employee',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='core.employee'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('Unresolved', 'Unresolved')], default='unresolved', editable=False, max_length=20),
        ),
    ]
