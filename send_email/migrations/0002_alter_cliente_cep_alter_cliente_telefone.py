# Generated by Django 5.0.3 on 2025-06-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(max_length=11),
        ),
    ]
