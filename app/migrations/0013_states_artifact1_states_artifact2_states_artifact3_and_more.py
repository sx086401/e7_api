# Generated by Django 4.2.2 on 2023-07-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_name_users_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='states',
            name='artifact1',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='states',
            name='artifact2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='states',
            name='artifact3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='states',
            name='exclusive_equipment',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]