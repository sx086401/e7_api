# Generated by Django 4.2.2 on 2023-07-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_characters_element_characters_star_alter_users_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='states',
            name='editor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
