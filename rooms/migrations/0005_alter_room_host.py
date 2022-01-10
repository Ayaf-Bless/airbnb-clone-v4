# Generated by Django 4.0 on 2022-01-10 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('rooms', '0004_alter_amenity_options_alter_facility_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='users.user'),
        ),
    ]
