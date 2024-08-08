# Generated by Django 5.0.2 on 2024-08-06 21:40

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('employee_number', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='category',
            field=models.CharField(choices=[('hardware', 'Hardware'), ('software', 'Software'), ('network', 'Network'), ('other', 'Other')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], default='medium', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('closed', 'Closed')], default='open', max_length=20),
        ),
        migrations.AddField(
            model_name='itasset',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assets', to='core.employee'),
        ),
    ]