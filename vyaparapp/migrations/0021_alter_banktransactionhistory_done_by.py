# Generated by Django 4.2.6 on 2023-11-17 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0020_banktransactionmodel_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banktransactionhistory',
            name='done_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='done_by_staff', to='vyaparapp.staff_details'),
        ),
    ]
