# Generated by Django 5.0.2 on 2024-08-07 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_itasset_employee_alter_ticket_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itasset',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='core.employee'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('hardware', 'Hardware'), ('software', 'Software'), ('network', 'Network'), ('it_support', 'IT Support'), ('other', 'Other')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('unresolved', 'Unresolved')], default='unresolved', editable=False, max_length=20),
        ),
    ]