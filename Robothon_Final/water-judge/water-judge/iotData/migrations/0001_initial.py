# Generated by Django 2.2 on 2020-02-29 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=250, null=True)),
                ('location_name', models.CharField(blank=True, max_length=250, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.IntegerField(default=0)),
                ('field2', models.IntegerField(default=0)),
                ('field3', models.IntegerField(default=0)),
                ('field4', models.IntegerField(default=0)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iotData.Sensor')),
            ],
        ),
    ]