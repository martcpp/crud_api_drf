# Generated by Django 4.2.5 on 2023-09-14 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.company'),
        ),
    ]
