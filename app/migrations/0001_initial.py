# Generated by Django 4.2.2 on 2023-06-29 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image_url', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='StateDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atk', models.IntegerField()),
                ('defense', models.IntegerField()),
                ('health', models.IntegerField()),
                ('spd', models.IntegerField()),
                ('cri', models.IntegerField()),
                ('crd', models.IntegerField()),
                ('eff', models.IntegerField()),
                ('res', models.IntegerField()),
                ('weapon', models.IntegerField()),
                ('helmet', models.IntegerField()),
                ('armor', models.IntegerField()),
                ('necklace', models.IntegerField()),
                ('ring', models.IntegerField()),
                ('boots', models.IntegerField()),
                ('weaponSet', models.CharField(max_length=50)),
                ('helmetSet', models.CharField(max_length=50)),
                ('armorSet', models.CharField(max_length=50)),
                ('necklaceSet', models.CharField(max_length=50)),
                ('ringSet', models.CharField(max_length=50)),
                ('bootsSet', models.CharField(max_length=50)),
                ('set1', models.CharField(max_length=50)),
                ('set2', models.CharField(max_length=50)),
                ('set3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.characters')),
                ('current_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_states', to='app.statedetails')),
                ('expect_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='expect_state', to='app.statedetails')),
            ],
        ),
    ]
