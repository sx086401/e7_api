# Generated by Django 4.2.2 on 2023-07-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_characters_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statedetails',
            name='armorSet',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='bootsSet',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='helmetSet',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='necklaceSet',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='ringSet',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='set1',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='set2',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='set3',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statedetails',
            name='weaponSet',
            field=models.CharField(blank=True, default='', max_length=50),
            preserve_default=False,
        ),
    ]
