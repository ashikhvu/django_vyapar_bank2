# Generated by Django 4.2.6 on 2023-11-15 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0016_banktransactionhistory_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='banktransactionhistory',
            name='bank_trans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vyaparapp.banktransactionmodel'),
        ),
    ]
