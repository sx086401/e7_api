# Generated by Django 4.2.2 on 2023-07-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_statedetails_armorset_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='characters',
            name='classes',
            field=models.CharField(default='mage', max_length=50),
            preserve_default=False,
        ),
    ]