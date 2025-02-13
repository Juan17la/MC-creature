# Generated by Django 5.1.6 on 2025-02-12 17:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_creature', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='creature',
            name='special_ability',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_creature.specialability'),
        ),
        migrations.AlterField(
            model_name='creature',
            name='stats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='create_creature.stats'),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
