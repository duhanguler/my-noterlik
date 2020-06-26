# Generated by Django 3.0.7 on 2020-06-26 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noterler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noterIli', models.CharField(max_length=255)),
                ('noterAdi', models.CharField(max_length=255)),
                ('noterAdiSoyadi', models.CharField(max_length=255)),
                ('noterlikSinifi', models.IntegerField(max_length=2)),
                ('noterSinifi', models.IntegerField(max_length=2)),
                ('noterAsilVekil', models.CharField(max_length=2)),
                ('noterTelefonu', models.CharField(max_length=16)),
                ('noterFaksi', models.IntegerField(max_length=16)),
                ('noterAdresi', models.CharField(max_length=255)),
                ('noterHarita', models.CharField(max_length=2080)),
            ],
        ),
    ]
